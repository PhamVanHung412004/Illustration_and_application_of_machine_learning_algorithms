from .add_path import add
add()

from package import Dict

class Rect:
    def __init__(self, type_rect : str, 
                x_rect : int, 
                y_rect : int, 
                width_rect : int, 
                height_rect : int,
                fill_rect : str,
                stroke_rect : str,
                strokeWidth : int) -> None:

        self.type_rect : str = type_rect
        self.x_rect : int = x_rect
        self.y_rect : int = y_rect
        self.width_rect : int = width_rect
        self.height_rect : int = height_rect
        self.fill_rect : str = fill_rect
        self.stroke_rect : str = stroke_rect
        self.strokeWidth : int = strokeWidth

    def Return_Information_Rect(self) -> Dict[str, str | int]:
        return {
            "type": self.type_rect,
            "left": self.x_rect,
            "top": self.y_rect,
            "width": self.width_rect,
            "height": self.height_rect,
            "fill": self.fill_rect,
            "stroke": stroke_rect,
            "strokeWidth": strokeWidth
        }




