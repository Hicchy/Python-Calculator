#addition
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1 , n2):
    return n1 * n2

#division
def divide(n1, n2):
    return n1 / n2

#a dictionary of operators 
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}