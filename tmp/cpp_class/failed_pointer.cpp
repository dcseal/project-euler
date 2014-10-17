#include <stdio.h>
#include <stdlib.h>

class A
{

    public:
    A();
    ~A();

    void set_operate(int n);
    int (A::*operate)(int a, int b );

    private:

    int a_plus_b (int a, int b);
    int a_minus_b(int a, int b);

};

A::A()
{ }

A::~A()
{ }

void set_operate( int n )
{
    if( n > 0 )
        operate = &A::a_plus_b;
    else
        operate = &A::a_plus_b;

}

int a_plus_b(int a, int b)
{
    return a+b;
}

int a_minus_b(int a, int b)
{
    return a-b;
}

int main( int argc, char** argv )
{

    A r;
    r.set_operate(1);
//  (r.*operate)(2,1);
    return 0;

}
