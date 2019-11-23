#include <stdio.h>
int main(){
    
    int n,m,i,j,totalComGol=0, semGol=0;

    scanf("%d", &n);
    scanf("%d", &m); 
  
    int matriz[n][m]; 

    for ( i = 0; i < n; i++) 
    {
        for ( j = 0; j < m; j++) 
        {
            scanf("%d", &matriz[i][j]); 
        }
    }

    for ( i = 0; i < n; i++) 
    {
        for ( j = 0; j < m; j++) 
        {
            if (matriz[i][j] == 0){
                semGol++;
                break;
            }
        }
    }

    totalComGol = n - semGol;
    printf("%d\n", totalComGol);
    return 0;
}
