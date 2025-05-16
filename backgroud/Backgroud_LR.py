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


def convert_text(string : str) -> str:
    '''
    string : đoạn văn bản muốn chuyển sang toàn bộ kí tự viết hoa
    '''
    return string.upper()


def BG_LR(error : float, space : int) -> List[Dict[str, str | int]]:
    '''
    error : Lỗi sinh ra của thuật toán hồi quy
    space : khoảng cách từ Backgroud LR -> Backgroud KNN
    '''

    const_value : int = 1750

    const_value += space

    value : int = -100

    value1 : int = 300

    base_objects = [
        Line("line", 50, 50 + const_value, 50, 50 + const_value +  750, "black", 4).Return_Information_Line(),
        Line("line", 50, 750 + const_value + 50, 1050, 800 + const_value, "black", 4).Return_Information_Line(),
        Text("text", 40, 30 + const_value, "▲", 24, "black").Return_Information_Text(),
        Text("text", 1045, 788 + const_value, "►", 24, "black").Return_Information_Text(),
        Text("text", 35, 800 + const_value, "0", 24, "black").Return_Information_Text(),
        Text("text", 25, 45 + const_value, "Y", 24, "black").Return_Information_Text(),
        Text("text", 1045, 805 + const_value, "X", 24, "black").Return_Information_Text(),
        Text("text", 370, 805 + const_value, "Illustration of regression algorithm", 24, "black").Return_Information_Text(),

        Rect("rect", 1080, 50 + const_value - value, value1, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1110, 70 + const_value - value, convert_text("Predict recipe") , 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 140 + const_value - value, value1,70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1095, 160 + const_value - value, convert_text("Delete the line 1"), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 230 + const_value - value, value1,70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1100, 250 + const_value - value, convert_text("Predict library"), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 320 + const_value - value, value1, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1095, 340 + const_value - value, convert_text("Delete the line 2"), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 410 + const_value - value, value1, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1095, 430 + const_value - value, convert_text("Error = ") + str(error), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 500 + const_value - value, value1, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1180, 520 + const_value - value, convert_text("Reset"), 30, "black").Return_Information_Text(),

        Rect("rect", 1080, 590 + const_value - value, value1, 70, "white", "black", 4).Return_Information_Rect(),
        Text("text", 1130, 610 + const_value - value, "APPLICATION", 30, "black").Return_Information_Text()
            
    ]
    return base_objects
