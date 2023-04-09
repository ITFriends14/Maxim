import turtle


turtle.color('black')

# for i in range(4):
#     turtle.right(40)
#     turtle.forward(100)

# for i in range(25):
#     turtle.right(15)
#     turtle.forward(10)

# num1 = 10
# num2 = 11

# num3 = num1 + num2

# if num1 !=num2:
#     print(f'{num1} не равно {num2}')
# elif type(num1) ==type(num2):
# eles:
#     print(f'{num1} равно {num2}')

# print(num3)

# while True:
#     num1 = int(input())
#     num2 = int(input())
#     s = input()

#     if type(num1) == type(num2):
#         if type(s) == str:
#             if s == "+":
#                 print(num1 + num2)
#             if s == "-":
#                 print(num1 - num2)
#             if s == "*":
#                 print(num1 * num2)
#             if s == "/":
#                 print(num1 / num2)
#                 ...
#             if s == "exit":
#                 break

while True:
    s = input('').split(',')

    if s[0] == "square" :
        for i in range(4):
            if len(s) > 1:
                turtle.right(int(s[1]))
                if len(s) > 2:
                    turtle.forward(int(s[2]))
                else:
                    turtle.right(int(s[1]))
                    turtle.forward(100)
    elif s[0] == "circle":
        for i in range(25):
            turtle.right(15)
            turtle.forward(10)
    else:
        break