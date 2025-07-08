#include <stdio.h>


int somma(int a, int b){
    int c;
    c = a + b;
    return c;
}

void stampa_somma(int a, int b){
    printf("La somma e' %d", somma(a,b));
}

int main(){
    stampa_somma(89,90);
    return 0;
}
