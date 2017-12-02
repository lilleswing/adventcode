package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func line_to_ints(line string) (response []int) {
	vars := strings.Fields(line);
	retval := make([]int, len(vars))
	for i := 0; i < len(vars); i++ {
		retval[i], _ = strconv.Atoi(vars[i])
	}
	return retval
}

func read_f(fname string) (data string) {
	dat, _ := ioutil.ReadFile(fname)
	return strings.Trim(string(dat), "\n")
}

func min(a []int) (m int) {
	b := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] < b {
			b = a[i]
		}
	}
	return b
}

func max(a []int) (m int) {
	b := a[0]
	for i := 0; i < len(a); i++ {
		if a[i] > b {
			b = a[i]
		}
	}
	return b
}

func day2_p1(input string) (retval string) {
	lines := strings.Split(string(input), "\n")
	total := 0
	for i := 0; i < len(lines); i++ {
		line := line_to_ints(lines[i])
		m1 := min(line)
		m2 := max(line)
		total += m2 - m1
	}
	return fmt.Sprintf("%d", total)
}

func p2_csum_line(a []int) (retval int, err int) {
	for i := 0; i < len(a); i++ {
		for j := i + 1; j < len(a); j++ {
			v1, v2 := a[i], a[j]
			if v1%v2 == 0 {
				return v1 / v2, 0
			}
			if v2%v1 == 0 {
				return v2 / v1, 0
			}
		}
	}
	return 0, 1
}

func day2_p2(input string) (retval string) {
	lines := strings.Split(string(input), "\n")
	total := 0
	for i := 0; i < len(lines); i++ {
		line := line_to_ints(lines[i])
		retval, _ := p2_csum_line(line)
		total += retval
	}
	return fmt.Sprintf("%d", total)
}

func main() {
	data := read_f("/Users/leswing/Documents/adventcode/2017/day02.in")
	fmt.Println(day2_p1(data))
	fmt.Println(day2_p2(data))
}
