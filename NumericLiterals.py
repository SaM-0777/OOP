a = 0b0010  #Binary Literals
b = 100     #Decimal Literals
c = 0o310   #Octal Literals
d = 0x02b    #Hexadecimal Literals

#Float Literals
x = 0.2354554

#Complex Literals
y = 5.23j
z = 10.45j
print(type(y))  ##Complex

print(a, b, c, d, x, y)
print(y + z)

#String Literals
z = "Kanha"
print(z)

#Boolean Literals
m = (1 == True)
n = (1 == False)
l = True + 5
o = False + 20
k = False
print(type(m))
print(type(o))
print("m is ", m)
print("n is ", n)
print("l:", l)
print("o:", o)
print("k is ", k)

#Special Literals
junk = None
food = "Available"
print(junk, food)
def Food(food):
    if food == "food":
        print("AVailable")
    else:
        print("Not Available")
Food(junk)
Food(food)

##Built-In Atomic data types
print(2 * 5)       ##Multiply
print(2 ** 5)       ##Exponent
print(20 / 5)       ##Division
print(15 % 7)       ##Reminder



#Literal Collections

#List (Sequence Data Type)
list1 = ["My", "Name", "is", "Soumya"]
list2 = ["Computer", "Science"]
print(type(list1))
print(list1)
print(list1 * 3)
print(list1 + list2)
print(list1[:3] + list2[-1:5])

#Tuple (Sequence Data type)
Numbers = (0, 5, 75, 10)
letters = ('a', 'b', 'c', 'd')
print(type(letters))
print(Numbers)
print(letters)
print(Numbers + letters)
print(Numbers[:2])
print(Numbers[:3] + letters[1:])

#Dictionary
data = {1 : "apple", 2 : "ball", 3 : "Cat"}
print(type(data))
print(data)
print(data[1])
print(data[2])
print(data.keys())
print(data.values())

#Set
set1 = {"a", "e", "i", "o", "u", True, 152, 175.369555, "Python"}
print(type(set1))
print(set1)
set1.add(15)
print(set1)
set1.remove("o")
#set1.remove(5) ##Indexing is not working...
print(set1)
