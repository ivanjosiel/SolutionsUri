#include <stdio.h>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

bool powOfTwo(int v){
    if (v == 1) return false;
    return v && !(v & (v - 1));
}

int main()
{
    int n, rita, uilton, ingred, u, r, i;
    string res;

    while (scanf("%d", &n) && n != 0)
    {
        rita = 0, uilton = 0, ingred = 0;
        for (size_t j = 0; j < n; j++)
        {
            scanf("%d %d %d", &u, &r, &i);
            if (powOfTwo(u)){
                uilton += 1;
                if (u > r && u > i)
                    uilton += 1;
            }
            if (powOfTwo(r)){
                rita += 1;
                if (r > u && r > i)
                    rita += 1;
            }
            if (powOfTwo(i)){
                ingred += 1;
                if (i > u && i > r)
                    ingred += 1;
            }
        }

        if (uilton > rita && uilton > ingred) res = "Uilton";
        else if (rita > uilton && rita > ingred) res = "Rita";
        else if (ingred > rita && ingred > uilton) res = "Ingred";
        else res = "URI";

        printf("%s\n", res.c_str());        

    }
    

    return 0;
}
