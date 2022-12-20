import random

words = ["umami","zumple","phlower","dark","pou","bro","mega","sigma","man","mind"]
numbers = [61,31,69,13,33,44,1001,41,11,88]

while True:
    print("\n\nPress \"F\" to create new username or quit with \"Q\" ")
    a = input()
    if a == 'F' or a == 'f':
        username = random.choices(words, k=2)
        num = random.choice(numbers)
        print(str(username[0]) + str(username[1]) + str(num))
        
    elif a == 'Q' or a == 'q':
        break
    
    else:
        print("Wrong input")

print("Program closed..")
