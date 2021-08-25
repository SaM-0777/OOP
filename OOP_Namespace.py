##Namespace in python

a = 1000
print(id(1000), id(a))  ##Refers to same ID
a += 1
print(id(1000), id(a))  ##Refers to different ID

##Scope in Python
##A small Portion of Program where namespace can be accessed without any prefix

a = 10
def Outerfunc():
    a = 20
    print(a)
    def Innerfunc():
        a = 40
        print(a)
    Innerfunc() ##Without this call it will throw a error

print(a)
Outerfunc()
