#include <iostream>
using namespace std;

class Student
{
    public :
    char Name[20], Subject[10];
    int age, RollNo;

    void Input()
    {
        cout<<"Enter your Name : ";
        cin>>Name;
        cout<<"Enter Age : ";
        cin>>age;
        cout<<"Enter Roll No : ";
        cin>>RollNo;
        cout<<"Enter Subject : ";
        cin>>Subject;
    }

    void Display()
    {
        cout<<"Name : "<<Name<<"\n";
        cout<<"Age : "<<age<<"\n";
        cout<<"ROll No : "<<RollNo<<"\n";
        cout<<"Subject : "<<Subject<<"\n";
    }
};

int main()
{
    Student s;
    s.Input();
    s.Display();
    cin.get();
    return 0;
}