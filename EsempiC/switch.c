#include <stdio.h>

int main()
{
    int scelta;
    printf("dammi un numero da 1 a 5: ");
    scanf("%d", &scelta);
    switch (scelta)
    {
    case 1:
        printf("\nBello mi piace il primo numero");
        break;
    case 2:
        printf("\nBello mi piace il secondo numero");
        break;
    case 3:
        printf("\nBello mi piace il terzo numero");
        break;
    case 4:
        printf("\nBello mi piace il quarto numero");
    case 5:
        printf("\nBello mi piace il quinto numero");
        break;
    default:
        printf("\nho detto da 1 a 5, cribbio! non era difficile!");
        break;
    }
    return 0;
}