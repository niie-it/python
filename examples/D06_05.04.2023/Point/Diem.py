from math import sqrt, pow
class Point:
    x: int = 0
    y: int = 0
    name: str = "no_name"
    
    def display(self):
        print(f"{self.name}({self.x}, {self.y})")
        
    def distance(self, other):
        '''Khoảng cách giữa điểm này (chính nó, self) đến điểm other'''
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
    
    def __init__(self, name = "noname", xx = 0, yy = 0) -> None:
        self.x = xx
        self.y = yy
        self.name = name
    
    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"