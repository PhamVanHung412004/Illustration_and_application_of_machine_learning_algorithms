import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
from typing import (
    List,
    Dict
)

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


def Get_Point( data : dict) -> list:
    try:
        point_x = data["path"][0][1: ]
        point_y = data["path"][1][1 : ]
        return point_x if (Check_Point(point_x,point_y)) else None
    except:
        return None

def init_Oxy() -> Dict[str, str | int]:
    return {
        "objects" : [
            {
                "type": "line",
                "x1": 0,
                "y1": 0,
                "x2": 1000,
                "y2": 0,
                "stroke": "black",
                "strokeWidth": 2
            },

            {
                "type": "line",
                "x1": 0,
                "y1": 0,
                "x2": 0,
                "y2": 660,
                "stroke": "black",
                "strokeWidth": 2
            }
        ]
    }

# Set up session state to store clicked points if it doesn't exist
if 'clicked_points' not in st.session_state:
    st.session_state.clicked_points = pd.DataFrame(columns=['x', 'y'])

st.markdown(colored_text("Pham Van Hung", "black"), unsafe_allow_html=True)

canvas_result = st_canvas(
    stroke_width=0,
    background_color="#ffffff",
    update_streamlit=True,
    height=650,
    width=750,
    initial_drawing= init_Oxy(),
    drawing_mode="freedraw",
    display_toolbar=False,
    key="canvas",
)


# Get the click coordinates
points_new = []
if canvas_result.json_data is not None:
    objects = canvas_result.json_data["objects"]
    points_new = [Get_Point(point) for point in objects if (Get_Point(point) != None)]
    print(points_new)


# st.title("Pham Van Hung")
