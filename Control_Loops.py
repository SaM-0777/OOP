###Control Loops in Python

##If...elif...else statement
a = 10
if a > 0:
    print("Positive")
elif a == 0:
    print("0")
else:
    print("Negative")
print(a)


##Loop in Python
num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0
for i in num:
    sum = sum + i
print(sum)

##Range function
list1 = list(range(10))
list2 = list(range(1, 10))
list3 = list(range(0, 10, 2))
print(list1, list2, list3)

##Looping with else statement
name = "Sam"
marks = {"Harry" : 50, "Edward" : 48, "John" : 40}
for student in marks:
    if student == name:
        print(marks[student])
        break

else:
    print("No student found with name", name)
