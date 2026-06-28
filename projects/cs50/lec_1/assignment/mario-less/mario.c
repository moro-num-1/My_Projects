#include <stdio.h>
#include <cs50.h>

//prototype funcs
void print_row(int bricks, int spaces);

int main(void)
{
    //Taking height
    int height;
    do
    {   
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    //Building the pyramid
    for (int i = 1, j = height; i <= height; i++, j--)
    {
        print_row(i, j);
    }

}

void print_row(int bricks, int spaces)
{
   //Space Brick 
    for (int i = 1; i <= spaces; i++)
    {
        printf(" ");
    }

    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");

}
