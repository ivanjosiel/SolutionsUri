#include <stdio.h>
#include <stdlib.h>

typedef struct lista{
	int info;
	struct lista* prox;	
}Lista;

typedef struct fila {
	/* os ponteiros ini e fim são do tipo lista */
	Lista* ini;
	Lista* fim;
}Fila;

Fila* criar(){
	Fila* f = (Fila*) malloc(sizeof(Fila)); /* aloca um espaço do tamanho de um tipo fina */
	f->ini = f->fim = NULL; /* os dois precisam apontar para nulo */
	return f;
}

void inserir(Fila* f, int v){
	Lista* n = (Lista*) malloc(sizeof(Lista)); /* aloca um novo nó */
	n->info = v; /* o campo info do novo nó armazena o valor que vai ser inserido na fila */
	n->prox = NULL; 
	if (f->fim != NULL) /* se a fila já conter algum valor (não estiver vazia) */
		f->fim->prox = n; /* o nó que o ponteiro fim já aponta (que aponta para null), agora apontará para o novo nó */
	else /* se a fila estiver vazia */
		f->ini = n; /* o novo nó vai ser o primeiro, então ini apontará pra ele (só ocorre uma vez) */
	f->fim = n; /* o ponteiro fim vai apontar para a nova inserção */
}

int retirar (Fila* f){
	/* cria um ponteiro auxi tipo lista, e uma variável tbm auxi */
	Lista* t;
	int v;
	/* se a fila estiver vazia, aborta o programa */
	if (f->ini == NULL){ 
		printf("Fila vazia\n");
		exit(1); 
		} 
	t = f->ini; /* ponteiro t aponta para o campo ini */
	v = t->info; /* variável armazena o valor do início ( que será retirado) */
	f->ini = t->prox; /* o ponteiro ini, apontará para o próximo do primeiro */
	if (f->ini == NULL) /* confere se após a retirada a lista ficou vazia */
		f->fim = NULL; /* se sim, o ponteiro fim tbm vai apontar para null */
	free(t); /* libera o nó t */
	return v; /* retorna o valor retirado */
}

/* função de inversão de número */
int inverter(int x){ /* recebe um valor para ser invertido */	
    int rest; /* armazenará o resto das divisões */
	int numInverso = 0; /* armazenará o valor invertido */
    while(x != 0){ /* enquanto x não for 0, divide-se ele por 10 guardando o resto das divisões */
        rest = x%10; /* gurranda o ultimo algarismo */
        numInverso = numInverso*10 + rest; /* multiplica o ultimo por 10 e soma o resto */
        x /= 10; /* divide o número por 10 mesmo */
    }
    return numInverso; 
}

/* função para zerar vetores */
void zera_vet (int *vet, int n){ /* recebe o vetor e seu tamanho */
	int i;
	for (i = 0; i < n; i++){ /* vai de 0 até o número correspondente ao tamanho do vetor */
		vet[i] = 0; /* atribui 0 a cada elemento do vetor */
	}
}

int main(){
	/* definindo variáveis e vetores */
	int teste, a, b, saiu;
	int somado=0, invertido=0;
	int verificaNum[10000];
	int botoes[10000];
	
	/* lendo os casos de teste */
	scanf("%d", &teste);
		
	/* enquanto o caso de teste não chegar em 0 */
	while (teste > 0){
		/* zerando os vetores */
		zera_vet (verificaNum, 10000);
		zera_vet (botoes, 10000);
		
		/* lendo o num que aparece no visor, e onde quer chegar */
		scanf("%d %d", &a, &b);
		
		/* criando a fila */
		Fila* fila; /* cria um ponteiro de tipo estruturado filla */
		fila = criar();
		
		/* insere o numero que aparece no visor na fila */
		inserir(fila, a); /* PARÂMETROS: o ponteiro da fila, e númoro do visor */
		
		/*  Marca no vetor que já passamos no a */
		verificaNum[a] = 1;	
		
		/* Se verifica no índice b estiver zero, significa que não chegamos ainda */
		while (verificaNum[b] == 0){
			saiu = retirar(fila);
			somado = saiu + 1;
			invertido = inverter(saiu);
			
			/* condição para os próximos daquele numero que foi retirado, no boão somar */
			if (verificaNum[somado] == 0  && saiu <= 10000){
				inserir(fila, somado); /* insere na fila o número somado +1 */
				botoes[somado] = botoes[saiu] + 1; /* incrementa no elemento do num somado */
				verificaNum[somado] = 1; /* marca no vetor de verificação que o num somado já foi verificado */
			}
			/* condição para o próximo, no botão de inverter */
			if (verificaNum[invertido] == 0 && saiu <= 10000){
				inserir(fila, invertido); /* insere na fila o num invertido */
				botoes[invertido] = botoes[saiu] + 1; /* incrementa no elemento do num invertido */
				verificaNum[invertido] = 1; /* marca no vetor de verificação que o num invertido já passou */
			}
		}
		teste--; /* O caso de teste é decrementado */
		   
		printf("%d\n", botoes[b]); /* o elemento com o índice b armazena o número mínimo de apertos de botões para chegar até ele*/
	}
	
	return 0;
}
