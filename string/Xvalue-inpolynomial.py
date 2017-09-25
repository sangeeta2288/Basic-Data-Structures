# Solve for X, eg:x+4 =9; x = 5

# 1.First lets workout solution for exact x + int = int format of the problem
# equation will be input from user in string format
# Time-
# Space-O(1)

def solve_equation(equation):
        x, op, num1,equal, num2 = equation.split()
        num1, num2 = int(num1), int(num2)
        if (op == "+"):
                return ("x= " + str(num2 - num1))

        elif(op == "-"):
                return ("x = " + str(num2 + num1))
        elif(op == "*"):
                return ("x = " + str(num2 / num1))
        elif(op == "/"):
                return ("x = " + str(num2 * num1))


