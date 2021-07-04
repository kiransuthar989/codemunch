 Make your Diet and Exercise schedule what u eat and perform exercise
 
# ** make a file to store data and retrieve from it
 
def getdate():
    import datetime
    return datetime.datetime.now()
time = getdate()   

#  Do you want to retrieve(0) or select treatment(1)                     
choose = int(input())

# Enter the member name karan, siddh, chef                                  
cm = input()

# Diet or Exercise
cd = input()

if choose == 1:
# Foods or Exercises
    value = input()
    def hfood(cm, cd):
        if cm ==  "siddh" and cd == "Diet":
            with open("Diet_1.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
               
        elif cm == "karan" and cd== "Diet":
            with open("Diet_2.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
               
        elif cm =="chef" and cd =="Diet":
            with open("Diet_3.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
                
    hfood(cm, cd)
    
    def fitnes(cm, cd):
        if cm =="siddh" and cd =="Exercise":
            with open("Exec_1.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
        elif cm == "karan" and cd == "Exercise":
            with open("Exec_2.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
        elif cm =="chef" and cd == "Exercise":                          
            with open("Exec_3.txt", "a") as d:
                d.write(str([str(time)]) + ":" + value + "\n")
                
    fitnes(cm, cd)
    
elif choose == 0:
    def hfood(cm, cd):
        if cm == "siddh" and cd == "Diet":
            with open("Diet_1.txt", "r") as d:                                                    
                print(d.read())   
          
        elif cm =="karan" and cd == "Diet":
            with open("Diet_2.txt", "r") as d:
                print(d.read())
        elif cm =="chef" and cd == "Diet":
            with open("Diet_3.txt", "r") as d:
                print(d.read())
                
    hfood(cm, cd)
    
    def fitnes(cm, cd):
        if cm == "siddh" and cd == "Exercise":
            with open("Exec_1.txt", "r") as d:
                print(d.read())
        elif cm == "karan" and cd == "Exercise":
            with open("Exec_2.txt", "r") as d:
                print(d.read())
        elif cm == "chef" and cd == "Exercise":
            with open("Exec_3.txt", "r") as d:
                print(d.read())
                
    fitnes(cm, cd)
