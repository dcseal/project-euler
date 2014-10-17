#include <stdio.h>
#include <stdlib.h>

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

    int n = -1;

    int (*operate)(int, int);
    if( n > 0 )
        operate = &a_plus_b;
    else
        operate = &a_minus_b;

    int result = (*operate)(1,2);

    printf(" result = %d\n", result );

    return 0;

}
