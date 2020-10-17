#include <iostream>
#include <string>
#include <stack>

using namespace std;


void reverseStr(string& str){
	int n = str.length();

	for (int i = 0; i < n/2; i++)
		swap (str[i], str[n-i-1]);
}

int main (){
	
	int n, ganhador = 0;
	char a;	
	int i, z;
	stack <string> brindeface;

	
	cin >> n;
	brindeface.push("FACE");

	for (z = 0; z < n; z++){
		
		string palavra;
		
		palavra.clear();

		for(i=0; i < 4; i++){

			cin >> a;
			palavra.push_back(a);
		}
		
		reverseStr(palavra);

		if (palavra == brindeface.top()){
			
			brindeface.pop();
			ganhador++;

			if (brindeface.empty()) brindeface.push("FACE");
		}
		else{
			reverseStr (palavra);
			brindeface.push(palavra);
		}	
	
	}
	printf ("%d\n", ganhador);

	return 0;
}
