#include <stdio.h>

int main(int argc, char *argv[]) {
	
	int n, r, vivos=0, i;
	
	while(scanf("%d %d", &n, &r) != EOF){
		int vet[n+1];
		
		for (i = 1; i <= n; i++){
			vet[i] = 0;
		}
		
		for (i = 0; i < r; i++){
			scanf("%d", &vivos);
			vet[vivos] = 1;
		}
		
		if(n == r){
			printf("*");
			
		}else{
			for (i = 1; i <= n; i++){
				if (vet[i] == 0){
					printf("%d ", i);
			}
		}
			
		}

		printf("\n");		
		
	}
	
	return 0;
}
