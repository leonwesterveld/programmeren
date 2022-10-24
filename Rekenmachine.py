import sys 
def add(a, b) :
    print(a+b)
    sys.exit()

def mult(a, b) :
    print(a*b)
    sys.exit()

def min(a, b) :
    print(a+b)
    sys.exit()

def deel(a, b) :
    print(a/b)
    sys.exit()


machine = input("+ - * /     ")
if machine == '+':
    add(int(input()), int(input()))
    add()
if machine == '-':
    min(int(input()), int(input()))
    min()
if machine == '*':
    mult(int(input()), int(input()))
    mult()
if machine == '/':
    deel(int(input()), int(input()))
    deel()