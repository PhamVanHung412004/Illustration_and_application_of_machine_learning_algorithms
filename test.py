import os
import streamlit as st
import streamlit.components.v1 as components
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import sqlite3
import requests

# ====== Khởi tạo DB SQLite ======
conn = sqlite3.connect("points.db", check_same_thread=False)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL,
    y REAL
)""")
conn.commit()

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

@app_api.post("/save")
def save_point(point: ClickPoint):
    c.execute("INSERT INTO clicks (x, y) VALUES (?, ?)", (point.x, point.y))
    conn.commit()
    return {"message": "Đã lưu vào database!"}

@app_api.get("/export")
def export_to_txt():
    # Lấy tất cả các điểm trong database
    rows = c.execute("SELECT x, y FROM clicks").fetchall()

    if rows:
        # Lưu các tọa độ vào file .txt
        file_path = "exported_points.txt"
        with open(file_path, "w") as file:
            for row in rows:
                file.write(f"{row[0]}, {row[1]}\n")
        return {"message": f"Dữ liệu đã được xuất vào {file_path}", "file": file_path}
    else:
        return {"message": "Không có dữ liệu nào để xuất."}

# Thêm route xóa tất cả dữ liệu
@app_api.delete("/clear")
def clear_all_data():
    c.execute("DELETE FROM clicks")
    conn.commit()
    return {"message": "Đã xóa tất cả dữ liệu khỏi database!"}

def run_api():
    uvicorn.run(app_api, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()


# ====== Streamlit app ======
st.title("Canvas HTML5 + JavaScript + Lưu vào SQLite")

components.html("""
<canvas id="myCanvas" width="600" height="400"
        style="border:1px solid #000000; background-color: white;"></canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Vẽ chấm
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = "black";
    ctx.fill();

    ctx.font = "14px Arial";
    ctx.fillStyle = "red";
    ctx.fillText(`(${event.clientX}, ${event.clientY})`, x + 10, y - 10);

    // Gửi POST request về API
    fetch("http://localhost:8000/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({x: x, y: y})
    })
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error("Lỗi:", error));
});
</script>
""", height=420)

# Thêm nút "Export" để tải dữ liệu về file .txt
if st.button("Tải về tọa độ dưới dạng .txt"):
    response = requests.get("http://localhost:8000/export")
    
    if response.status_code == 200:
        file_url = response.json().get("file")
        st.success(f"Dữ liệu đã được xuất. Bạn có thể tải về từ: {file_url}")
    else:
        st.error("Lỗi khi xuất dữ liệu!")

# Hiển thị dữ liệu đã lưu trong DB
st.subheader("📍 Các tọa độ đã lưu trong database:")
rows = c.execute("SELECT * FROM clicks").fetchall()
if rows:
    for row in rows:
        st.text(f"{row[0]}. ({row[1]}, {row[2]})")
else:
    st.write("Chưa có dữ liệu.")

# Thêm nút "Xóa tất cả dữ liệu"
if st.button("Xóa tất cả dữ liệu"):
    response = requests.delete("http://localhost:8000/clear")
    
    if response.status_code == 200:
        st.success("Đã xóa tất cả dữ liệu khỏi database.")
    else:
        st.error("Lỗi khi xóa dữ liệu.")
