#9th sep 8 ball
import random
def John():
    name = input("what is your name:")
    print("welcome", name, "to the 8 ball game")
    
John()

A = "yes absolutely"
B = "not a chance"
C = "maybe if you're lucky"
D = "very doubtful"
E = "you will find out soon"
F = "you will find out later in life"
G = "ask again"
H = "its better if you dont know"

question = input("what is your question?:")

print("shaking the 8 ball...")

choice = random.randint(1,8)

if choice == 1:
    answer = A
elif choice == 2:
    answer = B
elif choice == 3:
    answer = C
elif choice == 4:
    answer = D
elif choice == 5:
    answer = E
elif choice == 6:
    answer = F
elif choice == 7:
    answer = G
elif choice == 8:
    answer = H

print(answer)



