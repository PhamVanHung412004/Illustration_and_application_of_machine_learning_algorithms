# from .draw_rect import Rect
# from .draw_line import Line
# from .draw_text import Text
# from .draw_circle import Circle

# from .add_path import add
# add()

# from package import (
#     Dict,
#     List

# )


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



def BG_LR(error : float) -> List[Dict[str, str | int]]:
    '''
    error : Lỗi sinh ra của thuật toán hồi quy
    '''
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
    return base_objects
