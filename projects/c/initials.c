#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        printf("Give me any command line arguments\n");
        return 1;
    }
    for (int i = 1; i < argc; i++)
    {
        printf("%c", argv[i][0]);
    }
    printf("\n");
}
