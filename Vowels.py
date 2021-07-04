letters = list(input())
# print(letters)
vowels = [  letter.upper() 
            for letter in letters 
                if (letter := random.choice(letters)) in 
            list("aeoui")
         ]
print(vowels)
