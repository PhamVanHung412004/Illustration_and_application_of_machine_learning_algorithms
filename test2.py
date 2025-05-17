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
import matplotlib.pyplot as plt

# Khởi tạo session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    print(f"Tạo session mới: {st.session_state.session_id}")

# ====== Khởi tạo DB SQLite ======
DB_PATH = "points.db"
if os.path.exists(DB_PATH):
    print(f"Database found at: {os.path.abspath(DB_PATH)}")
else:
    print(f"Database not found, creating new one at: {os.path.abspath(DB_PATH)}")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# Tạo bảng nếu chưa tồn tại và kiểm tra schema
c.execute("""CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    x REAL,
    y REAL,
    timestamp INTEGER NOT NULL
)""")
conn.commit()

# Kiểm tra lại cấu trúc bảng
schema = c.execute("PRAGMA table_info(clicks)").fetchall()
print("Current schema of 'clicks':", schema)

# Thiết lập thời gian hết hạn cho session (10 phút = 600 giây)
SESSION_EXPIRY = 600

# Hàm để xóa session cũ khi ứng dụng thoát
def cleanup_old_sessions():
    print("Đang dọn dẹp các session cũ...")
    current_time = int(time.time())
    expiry_time = current_time - SESSION_EXPIRY
    c.execute("DELETE FROM clicks WHERE timestamp < ?", (expiry_time,))
    conn.commit()
    print(f"Đã xóa dữ liệu của các session cũ (hơn {SESSION_EXPIRY} giây).")

atexit.register(cleanup_old_sessions)

# ====== FastAPI server ======
app_api = FastAPI()

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

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        return str(uuid.uuid4())
    return session_id

@app_api.post("/save")
def save_point(point: ClickPoint):
    print(f"Click detected at coordinates: x={point.x}, y={point.y} for session: {point.session_id}")
    current_time = int(time.time())
    try:
        c.execute("INSERT INTO clicks (session_id, x, y, timestamp) VALUES (?, ?, ?, ?)", 
                  (point.session_id, point.x, point.y, current_time))
        conn.commit()
        return {"message": "Đã lưu vào database!"}
    except sqlite3.OperationalError as e:
        return {"error": f"Lỗi khi lưu vào database: {str(e)}"}

@app_api.get("/export/{session_id}")
def export_to_txt(session_id: str):
    try:
        rows = c.execute("SELECT x, y FROM clicks WHERE session_id = ? ORDER BY id", (session_id,)).fetchall()
        if rows:
            print(f"Exporting points for session {session_id}:")
            file_path = f"exported_points_{session_id}.txt"
            with open(file_path, "w") as file:
                for row in rows:
                    file.write(f"{row[0]}, {row[1]}\n")
            return {"message": f"Dữ liệu đã được xuất vào {file_path}", "file": file_path}
        else:
            return {"message": "Không có dữ liệu nào để xuất."}
    except sqlite3.OperationalError as e:
        return {"error": f"Lỗi khi truy vấn database: {str(e)}"}

@app_api.get("/draw/{session_id}")
def draw_image(session_id: str):
    try:
        rows = c.execute("SELECT x, y FROM clicks WHERE session_id = ? ORDER BY id", (session_id,)).fetchall()
        if rows:
            print(f"Drawing points for session {session_id}:")
            x_vals, y_vals = zip(*rows)
            plt.figure(figsize=(6, 4))
            plt.scatter(x_vals, y_vals, color='red')
            plt.plot(x_vals, y_vals, linestyle='--', color='blue')
            plt.title(f"Hình vẽ của Session: {session_id}")
            plt.grid(True)
            img_path = f"session_{session_id}.png"
            plt.savefig(img_path)
            plt.close()
            return {"message": f"Hình ảnh đã được lưu tại {img_path}", "file": img_path}
        else:
            return {"message": "Không có dữ liệu để vẽ."}
    except sqlite3.OperationalError as e:
        return {"error": f"Lỗi khi truy vấn database: {str(e)}"}
