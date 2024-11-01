# Define a class named HourlyWorker that has three private data members:
    # _name
    # _ID
    # _wage
# Give the class a DOCSTRING and __init__ method

class HourlyWorker:
    """HourlyWorker Object"""
    def __init__(self,name,id,wage):
        self._name = name
        self._id = id
        self._wage = wage

facebook = HourlyWorker("Mark", 777777, .0004)
girlswhocode = HourlyWorker("Reshma", 424242, 108.13)
print(facebook._name)
print(girlswhocode._wage)

class Box:
    """Box Object"""
    def __init__(self,length,width,height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height

    def surface_area(self):
        return self._length * self._width * 6

tesseract = Box(8, 8, 8)
print(tesseract.volume())
print(tesseract.surface_area())
print(tesseract._length)