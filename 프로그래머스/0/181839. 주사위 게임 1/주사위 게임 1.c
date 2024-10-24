#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) 
{
    if(a + b < 1 || a + b > 12)
        return -1;

    if(a % 2 != 0 && b % 2 != 0)
        return pow(a,2) + pow(b,2);

    else if(a % 2 != 0 || b % 2 != 0)
        return 2 * (a + b);

    else if(a % 2 == 0 && b % 2 == 0)
        return abs(a - b);
}