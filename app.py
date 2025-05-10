from package import (
    streamlit as st,
    st_canvas,
    pandas as pd,
    List,
    Dict,
    Image,
    ImageDraw
)

from backgroud import (
    Backgroud,
    Circle,
    Line,
    Rect
)

# setting fullscreen
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: white !important;
    }
    .stApp {
        background-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def Check_Point(point_x : list[float], point_y : list[float]):
    return point_x == point_y

def colored_text(text : str, color : str) -> str:
    return f"<span style='color:{color}'>{text}</span>"


def Get_Point(data : dict) -> list:
    try:
        point_x = data["path"][0][1 : ]
        point_y = data["path"][1][1 : ]
        return point_x
    except:
        return None

init_information_object = {
    "objects" : [
        Line("line",0,0,1000,0,"black",4).Return_Information_Line(),
        Line("line",0,0,0,700,"black",4).Return_Information_Line(),
        Line("line",996,0,996,700,"black",4).Return_Information_Line(),
        Line("line",0,700,1000,700,"black",4).Return_Information_Line(),
    ]
}

model = "freedraw"


# Set up session state to store clicked points if it doesn't exist
if 'clicked_points' not in st.session_state:
    st.session_state.clicked_points = pd.DataFrame(columns=['x', 'y'])


col1, col2 = st.columns([2,12])

with col2:
    canvas_result = st_canvas(
        stroke_width=2,
        background_color="#ffffff",  # Màu nền trắng
        update_streamlit=True,
        height=4000,    # Chiều cao của canvas
        width=1300,
        drawing_mode=model,
        initial_drawing = Backgroud(init_information_object).Show_Backgroud(),     # Chiều rộng của canvas
        display_toolbar=False,  # Bật toolbar để bạn dễ vẽ
        key="canvas",
    )


    # Get the click coordinates
    points_new = []
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        points_new = [Get_Point(point) for point in objects if (Get_Point(point) != None)]
        print(points_new)


# init_information_object["objects"].append(
#     {
#         "type": "rect",
#         "left": 100,
#         "top": 150,
#         "width": 200,
#         "height": 100,
#         "fill": "rgba(255, 165, 0, 0.3)",
#         "stroke": "#000000",
#         "strokeWidth": 3
#     }
# )

# canvas_result = st_canvas(
#     fill_color="rgba(0, 0, 255, 0.3)",  # Mặc định khi vẽ mới
#     stroke_width=3,
#     stroke_color="#000000",
#     background_color="#FFFFFF",
#     height=400,
#     width=600,
#     drawing_mode=model,  # Cho phép di chuyển, chỉnh sửa
#     initial_drawing=init_information_object,  # Toàn bộ dữ liệu hình
#     key="canvas"
# )

# canvas_result = st_canvas(
#     stroke_width=2,
#     background_color="#ffffff",  # Màu nền trắng
#     update_streamlit=True,
#     height=1000,    # Chiều cao của canvas
#     width=1000,
#     initial_drawing = Backgroud(init_information_object).Show_Backgroud(),     # Chiều rộng của canvas
#     drawing_mode=model,
#     display_toolbar=False,  # Bật toolbar để bạn dễ vẽ
#     key="canvas",
# )


# canvas_result = st_canvas(
#     stroke_width=2,
#     background_color="#ffffff",  # Màu nền trắng
#     update_streamlit=True,
#     height=1000,    # Chiều cao của canvas
#     width=1000,
#     initial_drawing = init_Oxy(),     # Chiều rộng của canvas
#     drawing_mode=model,
#     display_toolbar=False,  # Bật toolbar để bạn dễ vẽ
#     key="canvas",
# )
