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
    Rect,
    Text
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

def check_logic(x_begin : int ,x_mouse : int, x_max : int, y_begin : int, y_mouse : int, y_max : int) -> bool:
    return (x_begin <= x_mouse and x_mouse <= x_max) and (y_begin <= y_mouse and y_mouse <= y_max)

def Get_Point(data : dict) -> list:
    try:
        point_x = data["path"][0][1 : ]
        point_y = data["path"][1][1 : ]
        x_mouse = point_x[0]
        y_mouse = point_x[1]
        if (check_logic(50,x_mouse,1050, 50, y_mouse, 750)):
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            point_circle1 = Circle("circle",x_mouse - 10, y_mouse - 10,10, "black",2).Return_Information_Circle()
            point_circle2 = Circle("circle",x_mouse - 10, y_mouse - 10,10, "white",2).Return_Information_Circle()
            init_information_object["objects"].append(point_circle1)
            init_information_object["objects"].append(point_circle2)
        return point_x
    except:
        return None



# Set up session state to store clicked points if it doesn't exist
if 'clicked_points' not in st.session_state:
    st.session_state.clicked_points = pd.DataFrame(columns=['x', 'y'])

if 'drawn_objects' not in st.session_state:
    st.session_state.drawn_objects = []

col1, col2 = st.columns([1,10])
# print(init_information_object)
model = "freedraw"
with col2:
    canvas_result = st_canvas(
        stroke_width=2,
        background_color="#ffffff",  # Màu nền trắng
        update_streamlit=True,
        height=4000,    # Chiều cao của canvas
        width=1390,
        drawing_mode=model,
        initial_drawing = Backgroud(st.session_state.drawn_objects),     # Chiều rộng của canvas
        display_toolbar=False,  # Bật toolbar để bạn dễ vẽ
        key="canvas",
    )


    # Get the click coordinates
    # points_new = []
    # if canvas_result.json_data is not None:
    #     objects = canvas_result.json_data["objects"]
    #     points_new = [Get_Point(point) for point in objects if (Get_Point(point) != None)]
    #     if (points_new != []):
    #         print("aaaaaaaaaaaaaaa")
    #         print(points_new)
        
    #     st.rerun()
