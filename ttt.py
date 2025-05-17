import os
import streamlit as st
import streamlit.components.v1 as components
import threading
from fastapi import FastAPI, Depends, Cookie, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import sqlite3
import requests
import atexit
import uuid
from typing import Optional
import time

st.set_page_config(layout="wide")

# Khởi tạo session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    print(f"Tạo session mới: {st.session_state.session_id}")

# ====== Khởi tạo DB SQLite ======
conn = sqlite3.connect("points.db", check_same_thread=False)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    x REAL,
    y REAL,
    timestamp INTEGER NOT NULL
)""")
conn.commit()

# Thiết lập thời gian hết hạn cho session (10 phút = 600 giây)

# Hàm để xóa session cũ khi ứng dụng thoát

# ====== FastAPI server ======
app_api = FastAPI()

# CORS middleware
app_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ClickPoint(BaseModel):
    x: float
    y: float
    session_id: str



# Tạo session ID mới nếu chưa có
def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        return str(uuid.uuid4())
    return session_id


@app_api.post("/save")
def save_point(point: ClickPoint):
    print()
    print("hung hung")
    print("hung hung")
    # In tọa độ ra terminal mỗi khi nhận được click
    points_x_new = point.x
    points_y_new = point.y
    print('-' * 1000)
    print("y test : ", points_y_new)
    print(f"Click detected at coordinates: x = {abs(points_x_new)}, y = {abs(points_y_new - 400)} for session: {point.session_id}")
    
    # Lưu tọa độ cùng với session ID và timestamp
    current_time = int(time.time())
    c.execute("INSERT INTO clicks (session_id, x, y, timestamp) VALUES (?, ?, ?, ?)", 
              (point.session_id, point.x, point.y, current_time))
    conn.commit()
    return {"message": "Đã lưu vào database!"}

@app_api.get("/export/{session_id}")
def export_to_txt(session_id: str):
    # Lấy tất cả các điểm của session hiện tại
    rows = c.execute("SELECT x, y FROM clicks WHERE session_id = ? ORDER BY id", (session_id,)).fetchall()

    if rows:
        # In danh sách các điểm ra terminal
        # for row in rows:
        #     print(f"Point: {row[0]}, {row[1]}")
        
        # Lưu các tọa độ vào file .txt
        file_path = f"exported_points_{session_id}.txt"
        with open(file_path, "w") as file:
            for row in rows:
                file.write(f"{row[0]}, {row[1]}\n")
        return {"message": f"Dữ liệu đã được xuất vào {file_path}", "file": file_path}
    else:
        return {"message": "Không có dữ liệu nào để xuất."}

# Xóa dữ liệu của một session cụ thể
@app_api.delete("/clear/{session_id}")
def clear_session_data(session_id: str):
    c.execute("DELETE FROM clicks WHERE session_id = ?", (session_id,))
    conn.commit()
    return {"message": f"Đã xóa dữ liệu của session {session_id}!"}

# Thêm route để kiểm tra trạng thái kết nối
@app_api.get("/ping")
def ping():
    return {"status": "online"}

# Tạo session mới và trả về cookie
@app_api.get("/new_session")
def create_new_session(response: Response):
    session_id = str(uuid.uuid4())
    response.set_cookie(key="session_id", value=session_id)
    return {"session_id": session_id}

# Định kỳ xóa session cũ
@app_api.get("/cleanup")
def cleanup_old_data():
    current_time = int(time.time())
    expiry_time = current_time - SESSION_EXPIRY
    c.execute("DELETE FROM clicks WHERE timestamp < ?", (expiry_time,))
    deleted_count = c.rowcount
    conn.commit()
    return {"message": f"Đã xóa {deleted_count} bản ghi cũ."}

def run_api():
    uvicorn.run(app_api, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()

# Chạy dọn dẹp session cũ mỗi 5 phút



# ====== Streamlit app ======
st.title("Canvas HTML5 + JavaScript + Lưu vào SQLite")


# Hiển thị Session ID
st.sidebar.subheader("🔑 Session ID của bạn")
st.sidebar.code(st.session_state.session_id)
st.sidebar.info("💡 ID này giúp phân biệt dữ liệu của bạn với người dùng khác.", icon="ℹ️")

components.html(f"""
<canvas id="myCanvas" width="1000" height="4000"
        style="border:1px solid #000000; background-color: white;"></canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const sessionId = "{st.session_state.session_id}";

// Hàm gửi yêu cầu xóa dữ liệu của session này
function clearSessionData() {{
    fetch("http://localhost:8000/clear/" + sessionId, {{
        method: "DELETE"
    }})
    .then(response => response.json())
    .then(data => console.log("Đã xóa dữ liệu session:", data.message))
    .catch(error => console.error("Lỗi khi xóa dữ liệu session:", error));
}}

// Bắt sự kiện khi người dùng rời khỏi trang hoặc đóng trình duyệt
window.addEventListener('beforeunload', function(e) {{
    clearSessionData();
    // Đoạn code dưới đây tạo thông báo nhắc nhở khi người dùng đóng trang
    // Thông báo này có thể được hiển thị hoặc không tùy trình duyệt
    e.preventDefault();
    e.returnValue = '';
}});

// Tải dữ liệu cũ của session (nếu có)
function loadSessionData() {{
    fetch("http://localhost:8000/get_points/" + sessionId)
        .then(response => response.json())
        .then(data => {{
            if (data.points && data.points.length > 0) {{
                // Vẽ lại các điểm đã lưu
                data.points.forEach(point => {{
                    drawPoint(point.x, point.y);
                }});
                console.log("Đã tải " + data.points.length + " điểm từ session trước.");
            }}
        }})
        .catch(error => console.error("Lỗi khi tải dữ liệu:", error));
}}

// Hàm vẽ điểm
function drawPoint(x, y) {{
    // Vẽ chấm
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "black";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x, y, 4, 0, 2 * Math.PI);
    ctx.fillStyle = "white";
    ctx.fill();

    ctx.font = "14px Arial";
    ctx.fillStyle = "red";
    ctx.fillText(``, x + 10, y - 10);
}}

canvas.addEventListener("click", function(event) {{
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Vẽ điểm
    drawPoint(x, y);

    // Gửi POST request về API với tọa độ canvas chính xác và session ID
    fetch("http://localhost:8000/save", {{
        method: "POST",
        headers: {{
            "Content-Type": "application/json"
        }},
        body: JSON.stringify({{x: x, y: y, session_id: sessionId}})
    }})
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error("Lỗi:", error));
}});

// Tải dữ liệu khi trang được tải
document.addEventListener('DOMContentLoaded', loadSessionData);
</script>
""", height=4020)

# Thêm nút "Export" để tải dữ liệu về file .txt
if st.button("Tải về tọa độ dưới dạng .txt"):
    response = requests.get(f"http://localhost:8000/export/{st.session_state.session_id}")
    if response.status_code == 200:
        file_url = response.json().get("file")
        st.success(f"Dữ liệu đã được xuất. Bạn có thể tải về từ: {file_url}")
    else:
        st.error("Lỗi khi xuất dữ liệu!")

# Hiển thị dữ liệu đã lưu trong DB cho session hiện tại
st.subheader("📍 Các tọa độ đã lưu trong session của bạn:")
rows = c.execute("SELECT id, x, y FROM clicks WHERE session_id = ? ORDER BY id", 
                 (st.session_state.session_id,)).fetchall()
if rows:
    for row in rows:
        st.text(f"{row[0]}. ({row[1]}, {row[2]})")
else:
    st.write("Chưa có dữ liệu trong session này.")

# Hiển thị trạng thái của database
st.sidebar.subheader("⚙️ Trạng thái")
try:
    response = requests.get("http://localhost:8000/ping")
    if response.status_code == 200:
        st.sidebar.success("✅ Kết nối API: Hoạt động")
    else:
        st.sidebar.error("❌ Kết nối API: Lỗi")
except:
    st.sidebar.error("❌ Kết nối API: Không thể kết nối")

st.sidebar.info("📌 Khi bạn đóng trang web, chỉ dữ liệu của session của bạn sẽ bị xóa, không ảnh hưởng đến người dùng khác.", icon="ℹ️")

# Thêm nút "Xóa dữ liệu của session này"
if st.sidebar.button("🗑️ Xóa dữ liệu của session này"):
    response = requests.delete(f"http://localhost:8000/clear/{st.session_state.session_id}")
    
    if response.status_code == 200:
        st.sidebar.success("Đã xóa dữ liệu của session này.")
    else:
        st.sidebar.error("Lỗi khi xóa dữ liệu.")