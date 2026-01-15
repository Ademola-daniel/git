class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)

    def __str__(self):
        return f'({self.x,self.y})'


point1=Point(1,4)
point2=Point(2,3)

prin t(point1+point2)
