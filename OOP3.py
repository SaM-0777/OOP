#Problem 3\
s = "OOP Course is offered in IIIT DWD"
s = s.replace("OOP", "CS")
index = s.find("IIIT DWD")
if "IIIT DWD" in s:
    print("Inst. Found")
print(s, "\n", index)