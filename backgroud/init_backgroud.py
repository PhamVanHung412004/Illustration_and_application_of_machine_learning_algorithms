from package import (
    Dict,
    List
)

class Backgroud:
    def __init__(self, objects :  Dict[str, List[Dict[str, str]]]) -> None:
        self.objects :  Dict[str, List[Dict[str, str]]] = objects

    def Show_Backgroud(self) -> Dict[str, List[Dict[str, str]]]:
        return self.objects    
    