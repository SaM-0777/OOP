//Constructor in CPP
#include <iostream>
using namespace std;

class Adder
{  
    public :
        Adder(int i = 0)
        {
            total = i;
        }

        void AddNum(int Number)
        {
            total += Number;
        }

        int GetTotal()
        {
            return total;
        }
    
    private :
    int total;
};

int main(void)
{
    Adder obj;
    obj.AddNum(10);
    obj.AddNum(20);
    obj.AddNum(30);
    cout<<"Total : "<<obj.GetTotal();
    return 0;
}