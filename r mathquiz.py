import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operation = random.choice(OPERATORS)

    expr = str(left) + " " + operation + " " + str(right)
    answer = eval(expr)

    return expr, answer


print("Press Enter to Start")
print("====================")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problems()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
       

end_time = time.time()
total_time = round(end_time - start_time, 2) 

print("====================")
print("Nice work! The time taken was", total_time, "seconds")
