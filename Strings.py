##Strings in Python

inst = "IIIT Dharwad"
print(inst[:])
print(inst[::])
print(inst[:3])   ##Print first 3 characters
print(inst[-2:3])

##Slicing of String in Python
s = "Computer Science"
slice_1 = slice(-1, -6, -1)
slice_2 = slice(1, 6, -1)
slice_3 = slice(0, 5, 2)

print(s[slice_1])
print(s[slice_2])
print(s[slice_3])

##Reverse string using slicing
reverse_s = s[::-1]
print(reverse_s)

s1 = "Computer"
s2 = "Science"
print(s1 * 2)
print(s1, " " + s2)

