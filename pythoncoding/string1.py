import sys

# user defined function declaration

def student(Name, id):
    call = Name + ' ' + id
    return call

if __name__ == "__main__":
    Name = sys.argv[1]
    id = sys.argv[2]
    output = student(Name, id)
    print(output)


