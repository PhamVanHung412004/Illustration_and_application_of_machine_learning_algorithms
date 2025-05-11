import sys
import os
# thêm path thủ công 
def add():
    return sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
add()

from package import Dict
class Circle:
    def __init__(self, type_circle : str, 
                left_circle : int, 
                top_circle : int, 
                radius_circle : int, 
                fill_circle : str,
                strokeWidth : int) -> None:
        '''
        type_circle :   
        left_circle :  
        top_circle :  
        radius_circle :  
        fill_circle : 
        stroke_circle : 
        strokeWidth : 
        '''

        self.type_circle : str =  type_circle  
        self.left_circle : int = left_circle
        self.top_circle : int = top_circle
        self.radius_circle : int = radius_circle
        self.fill_circle : str = fill_circle
        self.strokeWidth : int = strokeWidth

    def Return_Information_Circle(self) -> Dict[str, str | int]:
        return { 
            "type": self.type_circle,
            "left": self.left_circle,
            "top": self.top_circle,
            "radius": self.radius_circle,
            "fill": self.fill_circle,
            "strokeWidth": self.strokeWidth
        }


