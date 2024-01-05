//--Summary:
//  Create a program that can read text from standard input and count the
//  number of letters present in the input.
//
//--Requirements:
//* Count the total number of letters in any chosen input
//* The input must be supplied from standard input
//* Input analysis must occur per-word, and each word must be analyzed
//  within a goroutine
//* When the program finishes, display the total number of letters counted
//
//--Notes:
//* Use CTRL+D (Mac/Linux) or CTRL+Z (Windows) to signal EOF, if manually
//  entering data
//* Use `cat FILE | go run ./exercise/sync` to analyze a file
//* Use any synchronization techniques to implement the program:
//  - Channels / mutexes / wait groups

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"sync"
	"time"
	"unicode"
)

type counter struct {
	count int
	sync.Mutex
}

func splitLine(line string) []string {
	return strings.Split(line, " ")
}

func count(wg *sync.WaitGroup, counter *counter, word string) {
	counter.Lock()
	defer wg.Done()
	defer counter.Unlock()

	count := 0
	for _, r := range word {
		if unicode.IsLetter(r) {
			count++
		}
	}
	counter.count += count
	fmt.Printf("word: %s, lettercount: %d\n", word, count)
}

func main() {
	start := time.Now()
	scanner := bufio.NewScanner(os.Stdin)

	var wg sync.WaitGroup
	var counter counter

	for scanner.Scan() {
		for _, word := range splitLine(scanner.Text()) {
			wg.Add(1)
			w := word
			go count(&wg, &counter, w)
		}
	}

	wg.Wait()

	var total int
	counter.Lock()
	total = counter.count
	counter.Unlock()
	fmt.Println("total", total)
	fmt.Println("duration", time.Since(start))
}
