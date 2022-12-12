import sys

def printtext(name):
    print("Hello world", "hi", name, sep=" - ")
    print("Hello world" + '' , name, end=".")

if __name__ == '__main__':
    printtext("Besant")
   
    printtext(sys.argv[1])

