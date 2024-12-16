import inspect
from dataclasses import dataclass
from pprint import pprint
@dataclass
class Comment:
    id: int
    msg: str
def main():
    comment=Comment(1,"Hello World")
    print(comment)
    pprint(inspect.getmembers(Comment,inspect.isfunction))
if __name__ == "__main__":
    main()