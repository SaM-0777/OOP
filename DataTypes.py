##Data Types in Python

#Containers
#List, Dictionary, Set and Tuples are Containers in Python

# 1. List
# A lisy in python is similar to array in C/C++, but resizable and contain element of different types

xs = [3, 2, 1]
print(xs, xs[2])
print(xs[-1])
xs[2] = "OOP"
print(xs)
xs.append("CS Course")
print(xs)
Temp = slice(1, 2, 1)
print(xs[Temp])
print(xs.pop())
print(xs)
print(xs[1:3])
xs[1:3] = [8, 9]
print(xs)
print(xs[:-1])
print(xs[-1:])
print(xs[:])
print(xs[len(xs) - 1:])

Num = list(range(10))
str = "20.1 + 90.4 + 78.5 + 40 + 45"
Temp = str.split("+")

sum = 0
for i in range(len(Temp)):
    sum += float(Temp[i])
print(sum)

animals = ["dog", "cat", "monkey"]
for animal in animals:
    if animal == "dog":
        print("Ok")
        break
    else:
        print("NO")

print(Num)
square = [x ** 2 for x in Num]
print(square)
##Num.append(x ** 2 for x in Num)   ##No Error but No result
##print(Num)
even_square = [x ** 2 for x in Num if x ** 2 % 2 == 0]
print(even_square)


# 2. Dictionary
# A Dictionary in Python is 
