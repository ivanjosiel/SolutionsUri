package problemas

import "fmt"

// Lê dois valores e retorna a soma deles
func Basico() {
	var a,b int

	fmt.Scanln(&a)
	fmt.Scanln(&b)

	fmt.Println("X = ", a+b)
}