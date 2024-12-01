import os

def create_file(name):
    f = open(name,'w')
    f.close()

def append_text(msg):
    try:
        with open("file.txt","a") as f:
            f.write(msg)
        print("Operation completed.")
    except IOError:
        "Couldn't complete operation."

def delete_file(name):
    try:
        os.remove(name)
        print(f"File ({name}) deleted successfully.")
    except IOError:
        "Couldn't complete operation."

if __name__ == '__main__':
    create_file('my_file.txt')
    delete_file('my_file.txt')