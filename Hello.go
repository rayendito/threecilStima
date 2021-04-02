package main

import "fmt"
import "math"

// import "rsc.io/quote"

type Simpul struct {
	Name    string
	Absis   float64
	Ordinat float64
	Index   int64
}

func euclidianDistance(x1, y1, x2, y2 float64) float64 {
	// ((y2-y1)^2 + (x2-x1)^2)^0.5
	return math.Pow(math.Pow(x2-x1, 2) + math.Pow(y2-y1,2), 0.5)
}

func main() {
	fmt.Println("Hello world")
	// var i int = 42
	// var j float64 = 32.02

	// fmt.Println(i)
	// fmt.Println(j)

	// newVertex := Simpul{Name: "Bandung", absis: 0, ordinat: 1, index: 100}
	// fmt.Println(newVertex.Name)
	// fmt.Println(newVertex.absis)
	// fmt.Println(newVertex.ordinat)
	// fmt.Println(newVertex.index)
	fmt.Println(euclidianDistance(0.0, 0.0, 3.0, 4.0))
}
