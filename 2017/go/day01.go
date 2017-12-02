package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func part1(dat string) (checksum int) {
	dat_s := dat + string(dat[0])
	total := 0
	for i := 1; i < len(dat_s); i++ {
		a1, _ := strconv.Atoi(string(dat_s[i-1]))
		a2, _ := strconv.Atoi(string(dat_s[i]))
		if a1 == a2 {
			total += a1
		}
	}
	return total
}

func part2(dat string) (checksum int) {
	total := 0
	half := len(dat) / 2;
	for i := 0; i < len(dat); i++ {
		index := (i + half) % len(dat)
		a1, _ := strconv.Atoi(string(dat[index]))
		a2, _ := strconv.Atoi(string(dat[i]))
		if a1 == a2 {
			total += a1
		}
	}
	return total

}

func main() {
	dat, _ := ioutil.ReadFile("/Users/leswing/Documents/adventcode/2017/day01.in")
	dat_s := strings.Trim(string(dat), "\n")
	fmt.Println(part1(dat_s))
	fmt.Println(part2(dat_s))
}
