sum = 10    ##Global Variables
var1 = 20
var2 = 30

print(type(var1))

print(id((var1)))   ##Object Identifieres
print(id(var2))


print(sum + var1 + var2)
def inner_func():
    a = 30          ##Local variables
    print("a : ", a)
inner_func()
##print(a)
##we cannot access local variables outside a function

"""Multiple variable Assignment"""
a = b = c = 40
d = e = 50
print(a + d)
Name = name = "Soumya Ranjan Sahu"
sem = 3
print(sem)
print(Name, name)



##Max possible value of Integers in python
c = 9999999999999999999999999999999999
print(c + 1)
print(type(c))

##Conversion between Datatypes
x = float(5)
y = int(15.256955)
z = float("25")
x2 = str("2056")
print(x, y, z, x2)

##Type conversion

##Implicit type Conversion
int_var = 10
float_var = 25.63
str_var = "580"
var = int_var + float_var
##var1 = int_var + str_var    ###Error
print("Data type of int_var : ", type(int_var))
print("Data type of float_var : ", type(float_var))
print("Data type of var : ", type(var))
##print("Data type of var1 : ", type(var1)) ###Error

##Explicit type Conversion
str_var = int(str_var)
print("Data type of str_var After Typecasting : ", type(str_var))
var1 = int_var + str_var
print("Data type of var1 : ", type(var1))

