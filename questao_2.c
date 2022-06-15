"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

#include <stdio.h>

/*----------------------------------*/
int fibonacci(int i){
    if ( i == 0 ){
        return 0;
    }
    else if ( i == 1){
        return 1;
    }
    else{
        return (fibonacci(i-1) + fibonacci(i-2));
    }
} 

/*----------------------------------*/
int main(){
	int n, i=1;
	printf("Digite o valor:\n");
	scanf("%d", &n);
    while (n > fibonacci(i)){
        i++;
        if (fibonacci(i) == n){
            printf("O número %d faz parte da sequencia de fibunacci", n);
        }
        else if (fibonacci(i) != n && fibonacci(i) > n){
            printf("O número %d não faz parte da sequencia de fibunacci", n);
        }
    }
}
    