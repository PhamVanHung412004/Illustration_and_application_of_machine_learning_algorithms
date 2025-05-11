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

        self.type_text : str = type_text
        self.left_text : int = left_text  
        self.top_text : int = top_text 
        self.text : str = text
        self.fontSize_text : int = fontSize_text,
        self.fill_text : str = fill_text

    def Return_Information_Text(self) -> Dict[str, str | int]:
        return {
                "type": self.type_text,
                "left": self.left_text,  # Tọa độ X của chữ
                "top": self.top_text,   # Tọa độ Y của chữ
                "text": self.text,
                "fontSize": self.fontSize_text,
                "fill": self.fill_text,
            }


