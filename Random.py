import random 
N = int(input())
a = 2 ** N

for j in range(a):
    count = 0
    fchoose = random.choice(['M', 'F'])
    print("family choose", fchoose)
    for i in range(a):
        choose = random.choice(['M', 'F'])
        print()
        print("try", choose)
        count += 1
        
        if choose == fchoose and i/a <= a/2:
            print(choose)
            
            break
    print(f"family {j + 1} try {count} ")
    print(20*'-')
