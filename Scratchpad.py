import pickle

class Student:
    def __init__(self,name):
        self._info={"Name":name}
    def save_data(self):
        with open('savefile.txt','wb') as f: #i could use f string to create different files depending on variables
            pickle.dump(self._info,f)

s = Student("Joe")
s.save_data()