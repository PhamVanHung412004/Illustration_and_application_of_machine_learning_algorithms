from .add_path import add
add()

from package import Dict

class Circle:
    def __init__(self, type_circle : str, 
                left_circle_x : int, 
                left_circle_y : int, 
                radius_circle : int, 
                fill_circle : str,
                strokeWidth : int) -> None:
        '''
        type_circle : tên của hình muốn vẽ
        left_circle_x : góc trên bên trái của trục hoành
        left_circle_y :  góc trên bên trái của trục tung
        radius_circle : bán kính của hình tròn muốn vẽ  
        fill_circle : màu của hình tròn đó
        strokeWidth : độ dày của hình tròn 
        '''

        self.type_circle : str =  type_circle  
        self.left_circle_x : int = left_circle_x
        self.left_circle_y : int = left_circle_y
        self.radius_circle : int = radius_circle
        self.fill_circle : str = fill_circle
        self.strokeWidth : int = strokeWidth

    def Return_Information_Circle(self) -> Dict[str, str | int]:
        return { 
            "type": self.type_circle,
            "left": self.left_circle_x,
            "top": self.left_circle_y,
            "radius": self.radius_circle,
            "fill": self.fill_circle,
            "strokeWidth": self.strokeWidth
        }


def main():
    print(Circle("circle",3,4,9,"black",4).Return_Information_Circle())

main()

