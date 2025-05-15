from .draw_rect import Rect
from .draw_line import Line
from .draw_text import Text
from .draw_circle import Circle

from .add_path import add
add()

from package import (
    Dict,
    List
)



def BG_KNN(n_clusters : int, K_KNN : int, space : int) -> List[Dict[str, str | int]]:
    '''
    n_clusters : số lượng cụm muốn phân của thuật toán KMeans
    n_knn : số lương k cụm gần với điểm mới đến nhất
    space : khoảng cách từ Backgroud KNN đến -> Backgroud KMeans
    '''
    const_value : int = 850
    const_value += space

    value : int = 40
    base_objects = [
        Line("line", 50, 50 + const_value, 50, 50 + const_value + 750 , "black", 4).Return_Information_Line(),
        Line("line", 50, 750 + const_value + 50, 1050, 800 + const_value, "black", 4).Return_Information_Line(),
        Text("text", 40, 30 + const_value, "▲", 24, "black").Return_Information_Text(),
        Text("text", 1045, 788 + const_value, "►", 24, "black").Return_Information_Text(),
        Text("text", 35, 800 + const_value, "0", 24, "black").Return_Information_Text(),
        Text("text", 25, 45 + const_value, "Y", 24, "black").Return_Information_Text(),
        Text("text", 1045, 805 + const_value, "X", 24, "black").Return_Information_Text(),
        Text("text", 370, 805 + const_value, "Illustration of the k-nearest neighbors algorithm", 24, "black").Return_Information_Text(),

        Rect("rect", 1080, 50 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 70 + const_value - value, "n_clusters = " + str(n_clusters), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 140 + const_value - value, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 150 + const_value - value, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 140 + const_value - value, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 145 + const_value - value, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 230 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 250 + const_value - value, "RUN KMEANS", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 320 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1150, 340 + const_value - value, "K_KNN = " + str(K_KNN), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 410 + const_value - value, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1125, 420 + const_value - value, "+", 45, "black").Return_Information_Text(),

        Rect("rect", 1230, 410 + const_value - value, 120, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1280, 420 + const_value - value, "-", 45, "black").Return_Information_Text(),

        Rect("rect", 1080, 500 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1105, 520 + const_value - value, "DELETE LABEL ", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 590 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1160, 610 + const_value - value, "RESET", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 680 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 697 + const_value - value, "ALGORITHM", 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 770 + const_value - value, 270, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1120, 790 + const_value - value, "APPLICATION", 30, "black").Return_Information_Text()
    ]
    return base_objects

