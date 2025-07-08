#include <stdio.h>

void scriviVettore(int *ptr)
{
    for (int i = 0; i < 10; i++)
    {
        printf("\nInserisci un numero: ");
        scanf("%d", ptr); // ovviamente e' gia' un puntatore e quindi non occorre &
        ptr++;
    }
}

void leggiVettore(int *ptr)
{
    for (int i = 0; i < 10; i++)
    {
        printf("\nElemento n[%d]\t=\t%d\tpuntatore: 0x%x", i, *ptr, ptr);
        ptr++;
    }
}

int main()
{
    int n[10] = {0};
    int *n_ptr;

    n_ptr=&n[0];

    scriviVettore(n_ptr);
    leggiVettore(n_ptr);

    return 0;

}