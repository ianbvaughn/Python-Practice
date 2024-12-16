class Disk:
    def __init__(self,size):
        self.size=size
    def __add__(self,other):
        if not isinstance(other,type(self)):
            raise TypeError(
                "Unsupported Operand! Cannot add classes of type "f"{type(self).__name__} and {type(other).__name__}"
            )
        return self.size+other.size

a = Disk(5)
b = str(10)
print(a+b)