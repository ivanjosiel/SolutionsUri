#include <stdio.h>

int buscaBinaria(int vetor[], int valor, int t) {  
	int posicaoEsquerda = 0;
	int posicaoDireita = t - 1;
	int posicaoMeio;
	while (posicaoEsquerda <= posicaoDireita) {
		posicaoMeio = (posicaoEsquerda + posicaoDireita) / 2;
		if (valor == vetor[posicaoMeio]) {
			return posicaoMeio;
		} else if (valor < vetor[posicaoMeio]) {
			posicaoDireita = posicaoMeio - 1; 
		} else if (valor > vetor[posicaoMeio]) {
			posicaoEsquerda = posicaoMeio + 1;
		}
	}
	return -1;
}

int main() {
    int N, i, j;
	int aux = 0;
	
	scanf("%d", &N);
	int vet[N];
	int t = N;
	
    for (i = 0; i < N; i++){
    	scanf("%d", &vet[i]);
		if (i == 0) {
           	aux = vet[i];
       	} else {
            vet[i] = vet[i - 1] + vet[i];
        }
	}
	
	int verf;
	int cont = 0;
	if ((vet[N-1] % 2) == 0) {
		int metade = vet[N-1] / 2;
		for (i = 0; i < N; i++) {
			
			//  Busca Binária
			verf = buscaBinaria(vet, (vet[i] + metade), N);
			if (verf != -1) {
				cont += 1;
			}
			
			
			/*  Busca Linear
			verf = buscaLinear(vet, (vet[i] + metade), N, i);
			if (verf != -1) {
				cont += 1;
			}
			*/
		}
		if (cont >= 2) {
			printf ("Y\n");
		} else {
			printf("N\n");
		}
	} else {
		printf("N\n");
	}
	
    return 0;
}
