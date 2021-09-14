class BinaryToDecimal:
    
    def Options(self):
        ch = int(input("Enter 1 for Decimal or 2 to Binary : "))
        if ch == 1:
            self.Binary()
        elif ch == 2:
            N = int(input("Enter Decimal Number : "))
            self.Decimal(N)
        else:
            print("Invalid Input")
    
    def Binary(self):
        result = 0
        i = j = 0
        print("Enter in Bits : ")
        while(j < 8):
            bit = int(input())
            if bit < 0 or bit > 1:
                print("Invalid Input")
                return
            else:
                i = 7 - j
                result += bit * (2 ** i)
                
            j += 1
        
        print("Decimal Equivalent : ", result)
    
    def Decimal(self, Binary):
        
        if Binary > 1:
            self.Decimal(Binary // 2)
        print(Binary % 2, end=' ')

B = BinaryToDecimal()
B.Options()