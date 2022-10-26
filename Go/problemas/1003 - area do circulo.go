package problemas

import "fmt"

// Essa funcao tambem retorna o falor de dois valores recebidos. 
// A diferença é apenas na hora de mostrar o resultado
func SomaValores2() {
	var a, b int

	fmt.Scanln(&a)
	fmt.Scanln(&b)

	fmt.Println("SOMA =", a+b)
}