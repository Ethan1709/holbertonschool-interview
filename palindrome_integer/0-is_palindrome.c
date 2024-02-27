#include <stdlib.h>
#include <stdio.h>

int is_palindrome(unsigned long n)
{
    unsigned long i = n;
    unsigned long reverse = 0;
    unsigned long temp;

    while (n != 0)
    {
        temp = n % 10;
        reverse = reverse * 10 + temp;
        n /= 10;
    }
    
    if (reverse == i)
        return 1;
    
    return 0;
}
