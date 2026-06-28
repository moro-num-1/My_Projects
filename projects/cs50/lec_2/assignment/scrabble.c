#include <stdio.h>
#include <cs50.h>
#include <string.h>

//Prototypes
int calc_scr(string word);

//Arrays
char a1[20] = {'a', 'A', 'e', 'E', 'i', 'I', 'l', 'L', 'n', 'N', 'o', 'O', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U'};
char a2[4] = {'d', 'D', 'g', 'G'};
char a3[8] = {'b', 'B', 'c', 'C', 'm', 'M', 'p', 'P'};
char a4[10] = {'f', 'F', 'h', 'H', 'v', 'V', 'w', 'W', 'y', 'Y'};
char a5[2] = {'k', 'K'};
char a8[4] = {'j', 'J', 'x', 'X'};
char a10[4] = {'q', 'Q', 'z', 'Z'};
//lengths of arrays
int l1 = sizeof(a1) / sizeof(char);
int l2 = sizeof(a2) / sizeof(char);
int l3 = sizeof(a3) / sizeof(char);
int l4 = sizeof(a4) / sizeof(char);
int l5 = sizeof(a5) / sizeof(char);
int l8 = sizeof(a8) / sizeof(char);
int l10 = sizeof(a10) / sizeof(char);


//Code
int main(void)
{
    //Assigning points to each letter ✅
    //Prompting the players for 2 words ✅
    //Summing up the points of entered letters for each input
    //Comparing both inputs to determine which player wins ✅
    string wrd1 = get_string("Player 1: ");
    string wrd2 = get_string("Player 2: ");
    int scr1 = calc_scr(wrd1);
    int scr2 = calc_scr(wrd2);
    if (scr1 > scr2)
    {
        printf("Player 1 wins!\n");
    }
    else if (scr2 > scr1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int calc_scr(string word)
{
    int scr = 0;
    for (int l = 0; l < strlen(word); l++)
    {
        for (int a = 0; a < l1; a++)
        {
            if (word[l] == a1[a])
            {
                scr++;
            }
        }
        for (int b = 0; b < l2; b++)
        {
            if (word[l] == a2[b])
            {
                scr += 2;
            }
        }
        for (int c = 0; c < l3; c++)
        {
            if (word[l] == a3[c])
            {
                scr += 3;
            }
        }
        for (int d = 0; d < l4; d++)
        {
            if (word[l] == a4[d])
            {
                scr += 4;
            }
        }
        for (int e = 0; e < l5; e++)
        {
            if (word[l] == a5[e])
            {
                scr += 5;
            }
        }
        for (int f = 0; f < l8; f++)
        {
            if (word[l] == a8[f])
            {
                scr += 8;
            }
        }
        for (int g = 0; g < l10; g++)
        {
            if (word[l] == a10[g])
            {
                scr += 10;
            }
        }
    }
    return scr;
}
