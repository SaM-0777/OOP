#include <iostream>
using namespace std;

class Encapsulation
{
    private :
        int num;
        char ch;
    
    public :
        int getNum()
        {
            return num;
        }
        char getCh()
        {
            return ch;
        }

        void setNum(int n)
        {
            num = n;
        }
        void setCh(char c)
        {
            ch = c;
        }
};

int main()
{
    int n;
    char ch;

    Encapsulation e;
    cout<<"Enter Num : ";
    cin>>n;
    e.setNum(n);
    cout<<"Num = "<<e.getNum()<<"\n";

    cout<<"Enter ch : ";
    cin>>ch;
    e.setCh(ch);
    cout<<"Ch = "<<e.getCh()<<"\n";
    return 0;
}