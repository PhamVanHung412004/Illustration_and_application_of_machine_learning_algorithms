import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Khởi tạo biến đếm trong session_state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Hiển thị biến đếm ra màn hình
st.markdown(f"### Số lần click: `{st.session_state.counter}`")

# Vẽ canvas
canvas_result = st_canvas(
    stroke_width=0,
    background_color="#ffffff",
    update_streamlit=True,
    height=400,
    width=600,
    drawing_mode="freedraw",
    display_toolbar=False,
    key="canvas",
)

# Xử lý sự kiện click
if canvas_result.json_data is not None:
    objects = canvas_result.json_data["objects"]
    for obj in objects:
        if obj["type"] == "path":
            path = obj["path"]
            x_mouse = path[0][1]
            y_mouse = path[0][2]
            if (x_mouse >= 0 and y_mouse >= 0):
                # Mỗi lần click, tăng biến đếm lên 1
                st.session_state.counter += 1
                
                # Cập nhật lại giá trị hiển thị
                st.markdown(f"### Số lần click: `{st.session_state.counter}`")
                break  # Chỉ lấy 1 lần click, tránh lặp
