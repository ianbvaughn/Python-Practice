import pickle

students = {
    "Student 1":{
        "Name":"Ian","Age":26,"Grade":14
    },
    "Student 2":{
        "Name":"Bob","Age":55,"Grade":19
    }
}
print(students)
with open('dbfile.txt','wb') as f:
    pickle.dump(students,f)
with open('dbfile.txt','rb') as i:
    students2 = pickle.load(i)
print(students2)