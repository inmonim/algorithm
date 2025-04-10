import "strconv"

func solution(n int) int {
	cnt := 0

	stringN := strconv.Itoa(n)

	i := 0
	for i < len(stringN) {
		cnt += int(stringN[i] - '0')
		i++
	}

	return cnt
}