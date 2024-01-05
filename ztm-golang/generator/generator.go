package main

import (
	"fmt"
	"math/rand"
	"time"
)

func generateRandIntn(count, min, max int) <-chan int {
	out := make(chan int, 1)

	go func() {
		for i := 0; i < count; i++ {
			out <- rand.Intn(max-min+1) + min
		}
		close(out)
	}()

	return out
}

func generateRandInt(min, max int) <-chan int {
	out := make(chan int, 3)

	go func() {
		for {
			out <- rand.Intn(max-min+1) + min
		}
	}()

	return out
}

func main() {
	rand.New(rand.NewSource(time.Now().UnixNano()))

	randInt := generateRandInt(1, 100)

	fmt.Println("generateRandInt infinite")
	fmt.Println(<-randInt)
	fmt.Println(<-randInt)
	fmt.Println(<-randInt)
	fmt.Println(<-randInt)
	fmt.Println(<-randInt)

	randIntn := generateRandIntn(2, 1, 10)

	fmt.Println("generateRandInt n")
	for i := range randIntn {
		fmt.Println("randIntn:", i)
	}

	randIntn2 := generateRandIntn(3, 1, 10)
	for {
		n, open := <-randIntn2
		if !open {
			break
		}
		fmt.Println("randIntn2:", n)
	}
}
