#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string letrs = get_string("Input: ");
    int l = 0;
    bool ordered = true;
    while (l < strlen(letrs) - 1)
    {
        if (letrs[l + 1] == letrs[l] + 1)
        {
            l++;
            continue;
        }
        else
        {
            ordered = false;
            break;
        }
    }
    if (ordered == true)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
}
