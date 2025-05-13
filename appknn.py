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

def colored_text(text: str, color: str) -> str:
    return f"<span style='color:{color}'>{text}</span>"

def check_logic(x_begin: int, x: int, x_end: int, y_begin: int, y: int, y_end: int) -> bool:
    return (x_begin <= x <= x_end) and (y_begin <= y <= y_end)

# Khởi tạo trạng thái
if 'clicked_plus' not in st.session_state:
    st.session_state.clicked_plus = False

if 'clicked_minus' not in st.session_state:
    st.session_state.clicked_minus = False

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'drawn_objects' not in st.session_state:
    st.session_state.drawn_objects = []

error = 0

def Backgroud(objects=[]) -> Dict[str, str | int]:
    base_objects = [
        Line("line", 50, 50, 50, 750, "black", 4).Return_Information_Line(),
        Line("line", 50, 750, 1050, 750, "black", 4).Return_Information_Line(),
        Text("text", 40, 30, "▲", 24, "black").Return_Information_Text(),
        Text("text", 1045, 738, "►", 24, "black").Return_Information_Text(),
        Text("text", 35, 750, "0", 24, "black").Return_Information_Text(),
        Text("text", 25, 45, "Y", 24, "black").Return_Information_Text(),
        Text("text", 1045, 760, "X", 24, "black").Return_Information_Text(),
        Text("text", 400, 760, "Illustration of kmeans algorithm", 24, "black").Return_Information_Text(),

        Rect("rect", 1080, 50, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 70, "n_clusters = " + str(st.session_state.counter), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 150, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 145, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 230, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1145, 250, "RANDOM", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 320, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1170, 340, "RUN", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 410, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 430, "ALGORITHM", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 500, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1105, 520, "ERROR = " + str(error), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 590, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1160, 610, "RESET", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 680, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 697, "APPLICATION", 30, "black").Return_Information_Text()
    ]
    return {"objects": base_objects + objects}
def Backgroud_KNN(objects=[]) -> Dict[str, str | int]:
    base_objects = [
        Line("line", 50, 50, 50, 750, "black", 4).Return_Information_Line(),
        Line("line", 50, 750, 1050, 750, "black", 4).Return_Information_Line(),
        Text("text", 40, 30, "▲", 24, "black").Return_Information_Text(),
        Text("text", 1045, 738, "►", 24, "black").Return_Information_Text(),
        Text("text", 35, 750, "0", 24, "black").Return_Information_Text(),
        Text("text", 25, 45, "Y", 24, "black").Return_Information_Text(),
        Text("text", 1045, 760, "X", 24, "black").Return_Information_Text(),
        Text("text", 370, 760, "Illustration of the k-nearest neighbors algorithm", 24, "black").Return_Information_Text(),

        Rect("rect", 1080, 50, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 70, "n_clusters = " + str(st.session_state.counter), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 150, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 145, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 230, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1145, 250, "RUN KMEANS", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 320, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1170, 340, "K KNN", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 410, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 420, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 410, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 420, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 500, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1105, 520, "DELETE LABEL ", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 590, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1160, 610, "RESET", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 680, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 697, "ALGORITHM", 30, "black").Return_Information_Text()
    ]
    return {"objects": base_objects + objects}

def Backgroud_LR(objects=[]) -> Dict[str, str | int]:
    base_objects = [
        Line("line", 50, 50, 50, 750, "black", 4).Return_Information_Line(),
        Line("line", 50, 750, 1050, 750, "black", 4).Return_Information_Line(),
        Text("text", 40, 30, "▲", 24, "black").Return_Information_Text(),
        Text("text", 1045, 738, "►", 24, "black").Return_Information_Text(),
        Text("text", 35, 750, "0", 24, "black").Return_Information_Text(),
        Text("text", 25, 45, "Y", 24, "black").Return_Information_Text(),
        Text("text", 1045, 760, "X", 24, "black").Return_Information_Text(),
        Text("text", 370, 760, "Illustration of regression algorithm", 24, "black").Return_Information_Text(),

        Rect("rect", 1080, 50, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 75, "Predict recipe" , 40, "black").Return_Information_Text(),

        Rect("rect", 1080, 170, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 195, "Delete the line 1", 40, "black").Return_Information_Text(),

        Rect("rect", 1080, 290, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 315, "Image", 40, "black").Return_Information_Text(),

        Rect("rect", 1080, 410, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 435, "Predict libxary", 40, "black").Return_Information_Text(),

        Rect("rect", 1080, 530, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 555, "Delete the line 2", 40, "black").Return_Information_Text(),

        Rect("rect", 1080, 650, 270, 100, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1085, 675, "Reset", 40, "black").Return_Information_Text()

        
    ]
    return {"objects": base_objects + objects}

col1, col2 = st.columns([2,9])
model:str = "freedraw"


with col2:
    st.subheader("Kmeans")
    canvas_result1 : st_canvas = st_canvas(
        stroke_width=0,
        background_color="#ffffff",
        update_streamlit=True,
        height=1000,
        width=1390,
        initial_drawing=Backgroud(st.session_state.drawn_objects),
        drawing_mode=model,
        display_toolbar=False,
        key="canvas1",
    )

    st.subheader("KNN")
    canvas_result2 : st_canvas = st_canvas(
        stroke_width=0,
        background_color="#ffffff",
        update_streamlit=True,
        height=1000,
        width=1390,
        initial_drawing=Backgroud_KNN(st.session_state.drawn_objects),
        drawing_mode=model,
        display_toolbar=False,
        key="canvas2",
    )

    st.subheader("Liner_Regression")
    canvas_result3 : st_canvas = st_canvas(
        stroke_width=0,
        background_color="#ffffff",
        update_streamlit=True,
        height=2000,
        width=1390,
        initial_drawing=Backgroud_LR(st.session_state.drawn_objects),
        drawing_mode=model,
        display_toolbar=False,
        key="canvas3",
    )

    if canvas_result1.json_data is not None:
        objects = canvas_result1.json_data["objects"]
        points_new = []

        for obj in objects:
            if obj["type"] == "path":
                path = obj["path"]
                x_mouse = path[0][1]
                y_mouse = path[0][2]

                if x_mouse >= 0 and y_mouse >= 0:
                    if check_logic(50, x_mouse, 1050, 50, y_mouse, 750):
                        new_circle_one = Circle("circle", x_mouse - 10, y_mouse - 10, 10, "black", 3).Return_Information_Circle()
                        new_circle_two = Circle("circle", x_mouse - 8, y_mouse - 8, 8, "white", 3).Return_Information_Circle()
                        points_new.extend([new_circle_one, new_circle_two])
                        with open("data.txt", "a") as file:
                            file.write(str([x_mouse - 50, abs(y_mouse - 750)]) + ",")

                # Button +
                if check_logic(1080, x_mouse, 1080 + 120, 140, y_mouse, 140 + 70):
                    if not st.session_state.clicked_plus:
                        st.session_state.counter += 1
                        st.session_state.clicked_plus = True
                        st.rerun()

                # Button -
                if check_logic(1230, x_mouse, 1230 + 120, 140, y_mouse, 140 + 70):
                    if not st.session_state.clicked_minus and st.session_state.counter > 0:
                        st.session_state.counter -= 1
                        st.session_state.clicked_minus = True
                        st.rerun()

        # Reset flags
        st.session_state.clicked_plus = False
        st.session_state.clicked_minus = False

        for obj in points_new:
            if obj not in st.session_state.drawn_objects:
                st.session_state.drawn_objects.append(obj)

        if points_new:
            st.rerun()








