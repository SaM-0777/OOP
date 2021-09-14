//Private Variables and Public Function

#include <iostream>
using namespace std;

class Rectangle
{
    private :
        int length, breadth;

    public :
        void Set(int l, int b)
        {
            length = l;
            breadth = b;
        }
        int GetLength()
        {
            return length;
        }
        int GetBreadth()
        {
            return breadth;
        }
        int GetArea()
        {
            return length * breadth;
        }
};

int main(void)
{
    Rectangle r;
    r.Set(25, 15);
    cout<<"Length : "<<r.GetLength()<<"\n";
    cout<<"Breadth : "<<r.GetBreadth()<<"\n";
    cout<<"Area : "<<r.GetArea();
    return 0;
}