#include <stdio.h>

int somma(int a, int b)
{
    int c;
    c = a + b;
    return c;
}

void stampa_somma(int a, int b)
{
    int som = somma(a, b);
    if (som < a && som < b)
    {
        printf("Qualcosa e' andato storto! %d + %d = %d?", a,b,som);
    }
    else
    {
        printf("La somma %d + %d = %d", a,b,som);
    }
}

int main()
{
    int a,b;
    printf("\nInserisci a: ");
    scanf("%d", &a);
    printf("\nInserisci b: ");
    scanf("%d", &b);
    stampa_somma(a, b);
    return 0;
}
