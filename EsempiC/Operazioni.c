#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int somma;

    printf("Ciao, dammi il primo numero: ");
    scanf("%d", &primo);
    printf("\nFigo! Mi piace il %d, dammi il secondo numero: ", primo);
    scanf("%d", &secondo);
    somma = primo + secondo;
    printf("\nLa somma e': %d", somma);
    printf("\nVoglio fare il figo, ti dico pure che la sottrazione e': %d", primo - secondo);
    printf("\nAh, dimenticavo, la moltiplicazione e' %d", primo * secondo);
    printf("\nScusa a mi taccio, la divisione e': %0.2f", (float) primo / (float) secondo);
    somma++;
    printf("\nE comunque il numero successivo alla somma e': %d", somma);
    secondo--;
    primo--;
    printf("\nFaccio un ipotesi, se mi avessi dato %d - %d, la sua somma sarebbe stata: %d", primo, secondo, primo + secondo);
    printf("\nnon per fare il figo il resto della divisione tra %d/%d e': %d", primo, secondo, primo % secondo);
    return 0;
}