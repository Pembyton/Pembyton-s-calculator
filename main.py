"""This is a calculator program
this calculator can add, subtract, mutliply, divide, exponet two number together
This calculator can also do some rounding"""
while True:
    addOrSub = input("add, subtract, mutliply, divide, exponent, or rounding?" )
    if addOrSub =="add": #add (The math sign is taken here)
        numb1 = float(input("the first number?" )) #The first number is taken here
        numb2 = float(input("the second number?" )) #The second number is taken here
        answer = float(numb1 + numb2) #The calculation is done here
        ANswer = (round(answer, 4)) #The answer is rounded to get a final answer
        print(numb1 , "+" , numb2 , "=" , ANswer) #The first number is printed the math sign is then printed, then the second number then the equals sign, at last the final answer
    if addOrSub =="subtract": #minus
        numb3 = float(input("the first number?" ))
        numb4 = float(input("the second number?" ))
        answer2 = float(numb3 - numb4,)
        ANswer2 = (round(answer2, 4))
        print(numb3 , "-" , numb4 , "=" , ANswer2)
    if addOrSub =="mutliply": #times
        numb5 = float(input("the first number?" ))
        numb6 = float(input("the second number?" ))
        answer3 = float(numb5*numb6,)
        ANswer3 = (round(answer3, 4))
        print(numb5 , "x" , numb6 , "=" , ANswer3)
    if addOrSub =="divide": #divides
        numb7 = float(input("the first number?" ))
        numb8 = float(input("the second number?" ))
        answer4 = float(numb7/numb8,)
        ANswer4 = (round(answer4, 4))
        print(numb7 , "/" , numb8 , "=" , ANswer4)
    if addOrSub =="exponent": # A to the power of B
        numb9 = float(input("the first number?" ))
        numb10 = float(input("the second number?" ))
        answer5 = float(numb9 ** numb10,)
        ANswer5 = (round(answer5, 4))
        print(numb9 , "^" , numb10 , "=" , ANswer5)
    if addOrSub =="rounding": # Rounding
        numb0 = float(input("the number?" ))
        print(round(numb0, 2))
    else:
        print("Error")
