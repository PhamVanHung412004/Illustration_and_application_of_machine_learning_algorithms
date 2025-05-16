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
    Text,
    BG_KMeans,
    BG_KNN,
    BG_LR
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


def colored_text(text : str, color : str) -> str:
    return f"<span style='color:{color}'>{text}</span>"

def check_logic(x_begin : int, x : int, x_end : int, y_begin : int, y : int, y_end : int) -> bool:
    return (x_begin <= x and x <= x_end) and (y_begin <= y and y <= y_end)

# click BG

if 'click' not in st.session_state:
    st.session_state.click : bool = False

# logic KMeans
if 'datas_KMeans' not in st.session_state:
    st.session_state.datas_KMeans : Dict[int, int] = {} 

if 'clicked_plus' not in st.session_state:
    st.session_state.clicked_plus : bool = False

if 'clicked_minus' not in st.session_state:
    st.session_state.clicked_minus : bool = False

if 'Parameter_BG_KMeans' not in st.session_state:
    st.session_state.Parameter_BG_KMeans : int = 0

if 'click_button_random' not in st.session_state:
    st.session_state.click_button_random : bool = False

if 'Erorr_KMeans' not in st.session_state:
    st.session_state.Erorr_KMeans : int = 0

# Logic button KNN
if 'height_BG_KNN' not in st.session_state:
    st.session_state.height_BG_KNN : int = 0
    
if 'clicked_plus_KMeans_in_KNN' not in st.session_state:
    st.session_state.clicked_plus_KMeans_in_KNN : bool = False

if 'clicked_minus_KMeans_int_KNN' not in st.session_state:
    st.session_state.clicked_minus_KMeans_int_KNN : bool = False

if 'clicked_plus_KNN' not in st.session_state:
    st.session_state.clicked_plus_KNN : bool = False

if 'clicked_minus_KNN' not in st.session_state:
    st.session_state.clicked_minus_KNN : bool = False

if 'counts_clusters_KMeans' not in st.session_state:
    st.session_state.counts_clusters_KMeans : int = 0

if 'counts_KNN' not in st.session_state:
    st.session_state.counts_KNN : int = 0

# logic BG LR
if 'height_BG_LR' not in st.session_state:
    st.session_state.height_BG_LR : int = 0

if "error_LR" not in st.session_state:
    st.session_state.error_LR : float = 0

if 'drawn_objects' not in st.session_state:
    st.session_state.drawn_objects : List[Dict[str , str | int]] = []

def Backgroud(objects = []) -> Dict[str, str | int]:
    init_BG_KMeans : List[Dict[str , str | int]] = BG_KMeans(st.session_state.Erorr_KMeans, st.session_state.Parameter_BG_KMeans)
    init_BG_KNN : List[Dict[str , str | int]] = BG_KNN(st.session_state.counts_clusters_KMeans, st.session_state.Parameter_BG_KMeans,st.session_state.height_BG_KNN)
    init_BG_LR : List[Dict[str , str | int]] = BG_LR(st.session_state.error_LR,st.session_state.height_BG_LR)

    meger_objects = init_BG_KMeans + init_BG_KNN + init_BG_LR 
    return {"objects": meger_objects + objects}

col1, col2 = st.columns([1,10])
model : str = "freedraw"

with col2:
    canvas_result : st_canvas = st_canvas(
        stroke_width=0,
        background_color="#ffffff",
        update_streamlit=True,
        height=4000,
        width=1390,
        initial_drawing=Backgroud(st.session_state.drawn_objects),
        drawing_mode=model,
        display_toolbar=False,
        key="canvas",
    )

    if canvas_result.json_data is not None:

        objects = canvas_result.json_data["objects"]

        # danh sách chứa tọa độ của 2 đường tròn lồng nhau
        points_new : List[List[Dict[str , str]]] = []    

        for obj in objects:
            if obj["type"] == "path":
                path = obj["path"]
                x_mouse = path[0][1]
                y_mouse = path[0][2]

                if (x_mouse >= 0 and y_mouse >= 0 and check_logic(50,x_mouse, 1050, 50, y_mouse, 750)):
                    if not st.session_state.click:                        
                        new_circle_one : Dict[str, str | int] = Circle("circle", x_mouse - 10, y_mouse - 10, 10, "black", 3).Return_Information_Circle()
                        new_circle_two : Dict[str, str | int] = Circle("circle", x_mouse - 8, y_mouse - 8, 8, "white", 3).Return_Information_Circle()
                        st.session_state.datas_KMeans[x_mouse - 50] = abs(y_mouse - 750)
                        points_new.extend([new_circle_one, new_circle_two])
                        st.session_state.click : bool = True

                # logic button +
                if (check_logic(1080, x_mouse, 1080 + 120, 140, y_mouse, 140 + 70)):
                    if not st.session_state.clicked_plus:
                        st.session_state.Parameter_BG_KMeans += 1
                        st.session_state.clicked_plus : bool = True
                        st.rerun()

                # logic button -
                if (check_logic(1230, x_mouse, 1203 + 120, 140, y_mouse, 140 + 70)):
                    if not st.session_state.clicked_minus and st.session_state.Parameter_BG_KMeans > 0:
                        st.session_state.Parameter_BG_KMeans -= 1
                        st.session_state.clicked_minus : bool = True
                        st.rerun()
                        
                if (check_logic(1080,x_mouse, 1080 + 270,230,y_mouse,230 + 70)):
                    if not st.session_state.click_button_random:
                        print("button random")
                        print("data: ",st.session_state.datas_KMeans)

                        st.session_state.click_button_random = True                     
                        st.rerun()

        st.session_state.click = False
        st.session_state.clicked_plus = False
        st.session_state.clicked_minus = False
        clicked_backgroud = False
        st.session_state.click_button_random = False                        


        for obj in points_new:
            if obj not in st.session_state.drawn_objects:
                st.session_state.drawn_objects.append(obj)
        if points_new:
            st.rerun()
        # print(check_datas)
