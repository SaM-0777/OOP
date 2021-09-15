def divideNum(Num_1, Num_2):
    try:
        print("Result : ", Num_1 / Num_2)
    except ZeroDivisionError:
        print("Zero is Invalid Argument")
    else:
        print("Else Block")

divideNum(10, 0)
divideNum(10, 4)