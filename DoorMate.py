N, M = input().split()

def UpperPart():
    for i in range(int(N)//2):
        a = (1 + i*2)*'.|.'
        print(a.center(int(M), '-'))
    MiddlePart()

def MiddlePart():
    print("WELCOME".center(int(M), '-'))
    BottomPart()
    
def BottomPart():
    for i in range(int(N)//2):
        a = ((1+(int(N)//2 - 1)*2) - i*2)*'.|.'
        print(a.center(int(M), '-'))
UpperPart()
