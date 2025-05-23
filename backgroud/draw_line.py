from .add_path import add
add()
from package import Dict

class Line:
    def __init__(self, type_line : str, 
                point_x_begin : int, 
                point_y_begin : int,
                point_x_end : int, 
                point_y_end : int,
                stroke_line : str,
                strokeWidth : int) -> None:
        ''' 
        point_x_begin : tọa độ x điểm đầu
        point_y_begin : tạo độ y điểm đầu
        point_x_end : tọa độ x điểm cuối
        point_y_end : tọa độ x điểm cuối
        stroke_line : màu của đoạn thẳng
        strokeWidth : độ dày của đoạn thẳng

        '''

        self.type_line : str = type_line 
        self.point_x_begin : int = point_x_begin
        self.point_y_begin : int = point_y_begin
        self.point_x_end : int = point_x_end
        self.point_y_end : int = point_y_end
        self.stroke_line : str = stroke_line
        self.strokeWidth : int = strokeWidth

    def Return_Information_Line(self) -> Dict[str, str | int]:
        return {
                "type": self.type_line,
                "x1": self.point_x_begin,
                "y1": self.point_y_begin,
                "x2": self.point_x_end,
                "y2": self.point_y_end,
                "stroke": self.stroke_line,
                "strokeWidth": self.strokeWidth
            }
    