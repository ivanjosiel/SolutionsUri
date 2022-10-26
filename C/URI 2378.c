#include <stdio.h>

int main()
{
    int n, c, s, e, i, x=0;
    scanf ("%d %d", &n, &c);
    for (i=1; i<=n; i++){
        scanf("%d %d", &s, &e);
        x = x - s;
        x = x + e;
        
        if (x>c){
            printf("S\n");
            return 0;
        }
        
    }
    if (x<=c){
        printf("N\n");
    }
    

    return 0;
}
