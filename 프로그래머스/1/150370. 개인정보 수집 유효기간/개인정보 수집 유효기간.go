import (
	"strconv"
	"strings"
)

func solution(today string, terms []string, privacies []string) []int {
	var answer []int

	todayDate := toDate(today)

	termMap := make(map[string]int)

	for _, term := range terms {
		termParts := strings.Split(term, " ")
		m, _ := strconv.Atoi(termParts[1])
		termMap[termParts[0]] = m
	}

	for i, privacy := range privacies {
		datePrivacy := strings.Split(privacy, " ")
		addM := termMap[datePrivacy[1]]
		targetDate := calcDate(toDate(datePrivacy[0]), addM)
		if isTimeout(targetDate, todayDate) {
			answer = append(answer, i+1)
		}
	}

	return answer
}

type Date struct {
	Y int
	M int
	D int
}

func toDate(stringDate string) Date {
	parts := strings.Split(stringDate, ".")
	Y, _ := strconv.Atoi(parts[0])
	M, _ := strconv.Atoi(parts[1])
	D, _ := strconv.Atoi(parts[2])
	return Date{Y: Y, M: M, D: D}
}

func calcDate(date Date, m int) Date {
	date.M += m
	ay := 0

	for date.M > 12 {
		date.M -= 12
		ay += 1
	}
	date.Y += ay

	return date
}

func isTimeout(date Date, now Date) bool {
	intDate := date.Y*10000 + date.M*100 + date.D
	intNow := now.Y*10000 + now.M*100 + now.D
	if intDate > intNow {
		return false
	}
	return true
}
