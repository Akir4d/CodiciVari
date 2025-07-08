#include <stdio.h>

int main()
{

    int n;
    int fattoriale=1;
    printf("dammi un numero e cerchero' di calcolare il fattoriale: ");
    scanf("%d", &n);
    // Salvo il numero in una varibile temporanea per poterlo stampare dopo
    int nn=n;
    while (n > 0){
        fattoriale = fattoriale*n;
        n--;
    }
    printf("\nil fattoriale di %d e' %d", nn, fattoriale);
    return 0;
}