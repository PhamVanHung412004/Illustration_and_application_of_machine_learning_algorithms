import streamlit as st
from PIL import Image, ImageDraw

# Tạo một ảnh trống (màu trắng) kích thước 400x300
width, height = 400, 300
image = Image.new("RGB", (width, height), "white")

# Vẽ hình chữ nhật
draw = ImageDraw.Draw(image)
# Tham số: (x1, y1, x2, y2) - tọa độ của hai điểm đối diện
draw.rectangle((50, 50, 200, 150), outline="blue", width=3)

# Hiển thị ảnh lên Streamlit
st.image(image, caption="Hình chữ nhật trong Streamlit")
