import streamlit as st
from streamlit_drawable_canvas import st_canvas
[{'type': 'circle', 'left': 680.998, 'top': 434, 'radius': 10, 'fill': 'blue', 'strokeWidth': 1}, {'type': 'circle', 'left': 339.998, 'top': 402, 'radius': 10, 'fill': 'blue', 'strokeWidth': 1}]
{'objects': [{'type': 'line', 'x1': 500, 'y1': 0, 'x2': 500, 'y2': 1000, 'stroke': 'black', 'strokeWidth': 2}, {'type': 'line', 'x1': 0, 'y1': 500, 'x2': 1000, 'y2': 500, 'stroke': 'black', 'strokeWidth': 2}, {'type': 'circle', 'left': 680.998, 'top': 434, 'radius': 10, 'fill': 'blue', 'strokeWidth': 1}, {'type': 'circle', 'left': 339.998, 'top': 402, 'radius': 10, 'fill': 'blue', 'strokeWidth': 1}]}
# Khởi tạo hệ tọa độ Oxy
def init_Oxy(objects=[]):
    print(objects)
    base_objects = [
        {
            "type": "line",
            "x1": 500,
            "y1": 0,
            "x2": 500,
            "y2": 1000,
            "stroke": "black",
            "strokeWidth": 2
        },
        {
            "type": "line",
            "x1": 0,
            "y1": 500,
            "x2": 1000,
            "y2": 500,
            "stroke": "black",
            "strokeWidth": 2
        }
    ]
    return {"objects": base_objects + objects}

# Khởi tạo session state để lưu các hình đã vẽ
if 'drawn_objects' not in st.session_state:
    st.session_state.drawn_objects = []


# Tạo canvas và render hình cũ
canvas_result = st_canvas(
    stroke_width=2,
    background_color="#ffffff",
    update_streamlit=True,
    height=1000,
    width=1000,
    initial_drawing=init_Oxy(st.session_state.drawn_objects),
    drawing_mode="freedraw",
    display_toolbar=False,
    key="canvas",
)

# Lấy tọa độ khi click
if canvas_result.json_data is not None:
    objects = canvas_result.json_data["objects"]
    for obj in objects:
        if obj["type"] == "path":
            path = obj["path"]
            x = path[0][1]
            y = path[0][2]

            # Tạo hình tròn tại tọa độ click
            new_circle = {
                "type": "circle",
                "left": x - 10,
                "top": y - 10,
                "radius": 10,
                "fill": "blue",
                "strokeWidth": 1
            }

            # Kiểm tra nếu chưa vẽ hình này thì thêm vào
            if new_circle not in st.session_state.drawn_objects:
                st.session_state.drawn_objects.append(new_circle)
    # print(type(init_Oxy(st.session_state.drawn_objects)))
    # Cập nhật lại canvas với các hình đã vẽ
    print(init_information_object)
    st.rerun()

