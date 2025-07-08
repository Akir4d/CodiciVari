#include <stdio.h>

int main()
{
    /*
    le varibili in c sono in realta' un assegnazione di un certo numero di byte 
    1, 2, 4, 8, 16 etc nella memoria.
    In pratica la ram che ha indirizzi di memoria viene organizzato in modo da riservare
    nel caso dell'int 32 bit
    le memorie hanno un indirizzo univoco che e' identificato come esadecimale
    */
    int primo_numero;

    printf("Inserisci il primo numero: ");
    /*
    scanf accetta 2 parametri, il primo e' rappresentato dal tipo di input che ci si aspetta
    %d sta per i valori numerici, %f sta per i valori float etc
    il secondo e' l'indirizzo di memoria della variabile che si ottiene anteponendo & alla varibile.
    */
    scanf("%d", &primo_numero);
    printf("\nhai inserito %d che si trova all'indirizzo di memoria 0x%x", primo_numero, &primo_numero);
    return primo_numero;
}

