from .draw_rect import Rect
from .draw_line import Line
from .draw_text import Text
from .draw_circle import Circle

import sys
import os
#add path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package import (
    Dict,
    List
)



def BG_KNN(n_clusters : int, n_knn : int) -> List[Dict[str, str | int]]:
    '''
    n_clusters : số lượng cụm muốn phân của thuật toán KMeans
    n_knn : số lương k cụm gần với điểm mới đến nhất
    '''
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
        Text("text", 1120, 70, "n_clusters = " + str(n_clusters), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 150, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 140, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 145, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 230, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1145, 250, "RUN KMEANS", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 320, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1170, 340, "K KNN = " + str(n_knn), 30, "black").Return_Information_Text(),

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

    return base_objects

