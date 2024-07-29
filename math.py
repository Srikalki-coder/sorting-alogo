#generate the random math probelm 
import random as n

count = 0
user_st = input("Do you want to start: ")

operator = ["+", "-", "*",]

def generate_math():
    turn = int(input("Enter to generate no o equations:"))
    for i in range(turn):
        
        left = n.randint(1, 20)
        right = n.randint(1,10)
        
        equation = f"{left} {operator[n.randint(0,2)]} {right}"
        user_answer = input(f"solve {equation}: ")
        answer = eval(equation)
        while True:
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == answer:
                    print("you got it")
                    break
                else:
                    user_answer = input(f"solve {equation}: ")
            else:
                print("Enter the valid number")
                user_answer = input(f"solve {equation}: ")
        

generate_math()

    
