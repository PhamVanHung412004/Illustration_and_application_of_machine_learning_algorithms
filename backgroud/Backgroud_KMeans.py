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


def BG_KMeans(n_clusters : int, error : float) -> List[Dict[str, str | int]]:
    '''
    n_clusters : Số cụm muốn phân của thuật toán KMeans
    error : số lỗi của thuật toán khi sử dụng
    '''
    data_backgroud : List[Dict[str, str | int]] = [
        Line("line",50,50,50,750,"black",4).Return_Information_Line(),
        Line("line",50,750,1050,750,"black",4).Return_Information_Line(),
        Text("text",40,30,"▲",24,"black").Return_Information_Text(),
        Text("text",1045,738,"►",24,"black").Return_Information_Text(),
        Text("text",35,750,"0",24,"black").Return_Information_Text(),
        Text("text",25,45,"Y",24,"black").Return_Information_Text(),
        Text("text",1045,760,"X",24,"black").Return_Information_Text(),
        Text("text",400,760,"Illustration of kmeans algorithm",24,"black").Return_Information_Text(),

        # Button n_clusters
        Rect("rect",1080,50,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1120,70,"n_clusters = " + str(n_clusters),30,"black").Return_Information_Text(),

        # Button +
        Rect("rect",1080,140,120,70,"white","black",4).Return_Information_Rect(),
        Text("text",1125,150,"+",45,"black").Return_Information_Text(),

        # Button -
        Rect("rect",1230,140,120,70,"white","black",4).Return_Information_Rect(),
        Text("text",1280,145,"-",45,"black").Return_Information_Text(),
        
        # Button RANDOM
        Rect("rect",1080,230,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1145,250,"RANDOM",30,"black").Return_Information_Text(),

        # Button RUN
        Rect("rect",1080,320,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1170,340,"RUN",30,"black").Return_Information_Text(),
        
        # Button ALGORITHM
        Rect("rect",1080,410,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1125,430,"ALGORITHM",30,"black").Return_Information_Text(),
        
        # Button ERROR
        Rect("rect",1080,500,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1105,520,"ERROR = " + str(error),30,"black").Return_Information_Text(),
        
        # Button RESET
        Rect("rect",1080,590,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1160,610,"RESET",30,"black").Return_Information_Text(),
        
        # Button Application
        Rect("rect",1080,680,270,70,"white","black",4).Return_Information_Rect(),
        Text("text",1120,697,"APPLICATION",30,"black").Return_Information_Text()
    ]
    return data_backgroud    


