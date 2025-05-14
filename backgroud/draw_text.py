# from .add_path import add
# add()

from typing import Dict


class Text:
    def __init__(self,
                type_text : str,
                left_text  : int,  
                top_text : int, 
                text : str,
                fontSize_text : int,
                fill_text : str) -> None:
        '''
        type_text : kiểu dữ liểu của văn bản(text)
        left_text : tọa độ góc trên bên phải của đoạn văn bản của trục hoành
        top_text : tọa độ góc trên bên phải của đoạn văn bản của trục tung
        text : văn bản muốn hiển thị
        fontSize_text : kích thước của chữ
        fill_text : màu của chữ
        '''

        self.type_text : str = type_text
        self.left_text : int = left_text  
        self.top_text : int = top_text 
        self.text : str = text
        self.fontSize_text : int = fontSize_text,
        self.fill_text : str = fill_text

    # Trả về thông tin của hình tròn
    def Return_Information_Text(self) -> Dict[str, str | int]:
        return {
                "type": self.type_text,
                "left": self.left_text,  # Tọa độ X của chữ
                "top": self.top_text,   # Tọa độ Y của chữ
                "text": self.text,
                "fontSize": self.fontSize_text,
                "fill": self.fill_text,
            }


def main():
    print("ahunaa")

main()