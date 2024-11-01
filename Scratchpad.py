class Point:
    """Represents a point in 2D space"""

    def __init__(self,x,y):
        self._xcoord = x
        self._ycoord = y

    def x_halved(self):
        return self._xcoord / 2

a = Point(30,150)
b = a.x_halved()
print(b)