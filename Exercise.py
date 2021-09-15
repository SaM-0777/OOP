##Exercise 

##Problem 1
def Max(Num1, Num2):
    if Num1 >= Num2:
        return Num1
    else:
        return Num2
print("Max Valuse : ", Max(20, 15))

##Problme 2
def numberGame(Num):
    if Num % 3 == 0:
        return "number"
    elif Num % 5 == 0:
        return "Game"
    elif Num % 3 == 0 and Num % 5 == 0:
        return "numberGame"
    else:
        return Num

print("Number : ", numberGame(9))


##Problem 4
def Driver(Speed):
    if Speed < 70:
        return "Ok"
    else:
        Speed = (Speed - 70) // 5
        if Speed > 12:
            print("License Suspended")
        return Speed

print(Driver(150))


##Problem 5
def showNumbers(limit):
    x = list(range(limit + 1))
    for i in x:
        if i % 2 == 0:
            print(i, "Even")
        else:
            print(i, "Odd")
showNumbers(3)

##Problem 6
def showSigns(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("&", end="")
        print()
showSigns(5)

##Problem 7
def Prime(max):
    def isPrime(N):
        c = 0
        for i in range(1, N//2 + 1):
            if N % i == 0:
                c += 1
        if c > 1:
            return False
        else:
            return True
    for i in range(1, max + 1):
        if isPrime(i):
            print(i, end=" ")
Prime(10)

##    -:End:-    ##