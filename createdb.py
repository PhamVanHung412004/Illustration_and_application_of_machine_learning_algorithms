import sqlite3

# Kết nối (hoặc tạo mới) database points.db
conn = sqlite3.connect("points.db")

# Tạo cursor
c = conn.cursor()

# Tạo bảng clicks nếu chưa có
c.execute("""
CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL,
    y REAL
)
""")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("✅ Đã tạo database points.db và bảng clicks.")
