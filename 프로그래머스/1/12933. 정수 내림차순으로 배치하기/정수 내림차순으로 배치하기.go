import (
    "strconv"
    "sort"
)

func solution(n int64) int64 {
    s := strconv.Itoa(int(n))
    runes := []rune(s)
    
    sort.Slice(runes,
               func(i, j int) bool {
                    return runes[i] > runes[j]
    })
    
    sortedString := string(runes)
    answer, _ := strconv.Atoi(sortedString)
    
    return int64(answer)
}