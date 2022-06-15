"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

#include <stdio.h>
#include <stdlib.h>

/*----------------------------------------*/

typedef struct nodo{
	char c;
	struct nodo *prox;
}NODO;

/*----------------------------------------*/

void inserirPilha(NODO **inicio, char c){
	NODO *nodo = (NODO *)malloc(sizeof(NODO));
	nodo->c = c;
	nodo->prox = NULL;
	
	nodo->prox = *inicio;
	*inicio = nodo;
}

/*----------------------------------------*/

void print(NODO *inicio){
	while ( inicio != NULL ){
		printf("%c", inicio->c);
		inicio = inicio->prox;
	}
}

/*----------------------------------------*/

int main(){
	
	NODO *pilha = NULL;
	NODO *fila_ini = NULL, *fila_fim = NULL;
	char c;
	
	printf("Termine a string com o caracter '.' para sair)\n");
	
	do{
		while ( (c = getchar()) == '\n');
			
		if (c!='.' ){
			inserirPilha(&pilha, c);
			}
	}
	while ( c != '.');
	
	print(pilha);

}
/*----------------------------------------*/

