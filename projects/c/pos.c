#include <stdio.h>
#include <cs50.h>

void chg_p(int x, int y);

int main(void)
{
    string choice;
    while (choice != "q")
    {
        choice = get_string("Choice: ");
        if (choice == "change")
        {
            int x = get_int("X: \n");
            int y = get_int("Y: \n");
            chg_p(x, y);
        }
        else if (choice == "read")
        {
            //Do This
        }
        else if (choice == "reset")
        {
            //Do This
        }
        else
        {
            printf("Invalid choice!!\n");
        }
    }

}

//function to change position
void chg_p(int x, int y)
{
   for (int i = 0; i < x; i++)
   {
       printf(" ");
   } 
   for (int i = 0; i < y; i++)
   {
       printf("\n");
   }
   printf("#");

}
