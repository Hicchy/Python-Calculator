#calculator

from functions1 import *
from art import logo

#function = operators["+"]
#function(2,3)


def calculator():
    print (logo)
    #continuity
    proccessDone = False
    #inputs from the user
    num1 = float(input("What's the first number?: "))
    #looping through the operators to give user feedback on what operations they have access to
    for x in operators:
        print (x)


    while not proccessDone: 
        
        #another one
        opAsk = input("What operation would you like to do?: ")
        num2 = float(input("What's the second number?: "))
        #calling the function according to user input
        function = operators[opAsk]
        answer = function(num1, num2)
        #final result
        print (f"{num1} {opAsk} {num2} = {answer}")
        qqq = input("Type 'y' to continue and 'n' to exit or 'r' to start over. ")
        if qqq == 'y':
            num1 = answer
        elif qqq == 'r':
            calculator()
        elif qqq == 'n':
            proccessDone = True

calculator()
