#include <stdio.h>
#include <cs50.h>

bool valid_trig(float s1, float s2, float s3);

int main(void)
{
    printf("%d\n", valid_trig(1, 2, 3));
}

bool valid_trig(float s1, float s2, float s3)
{
    //1+2 1+3 2+3 
    if (s1 < 1 || s2 < 1 || s3 < 1)
    {
        return false;
    }
    else
    {
        if (s1+s2 >= s3 && s1+s3 >= s2 && s2+s3 >= s1)
        {
            return true;
        }
        return false;
    }
}
