#include <stdio.h>

int main()
{
    int numeratore;
    int denominatore;
    float divisione;

    printf("Ciao, dammi il numeratore: ");
    scanf("%d", &numeratore);
    printf("\ndammi il denominatore: ");
    scanf("%d", &denominatore);
    if(denominatore == numeratore) {
        printf("Buffo, denomnatore e numeratore sono uguali");
    }
    /*
     nel caso di un singolo comando le {} possono essere omesse
    */
    if(denominatore != numeratore) printf("\nFigo, denominatore e numeratore sono diversi!");
    if(denominatore > numeratore) printf("\nPare che il denominatore sia maggiore");
    if(denominatore < numeratore) printf("\nPare che il denominatore sia inferiore");
    if(denominatore >= numeratore) printf("\nPare che il denominatore sia maggiore o uguale");
    if(denominatore <= numeratore) printf("\nPare che il denominatore sia inferiore o uguale");
    if(denominatore !=0 && numeratore !=0) printf("\nbuon segno! entrambi non sono 0!");
    if(denominatore > 0 || numeratore > 0) printf("\nNon serve a nulla ma uno dei sue e' maggiore di 0!");
    if(!(denominatore !=0 && numeratore !=0)) printf("\ncattivo presagio! uno dei due e' zero!");
    if (denominatore != 0){
        printf("\nil risultato della divisione e': %f", (float)numeratore/(float)denominatore);
    } else {
        printf("\nil denominatore non puo' essere 0!");
    }

    return 0;
}