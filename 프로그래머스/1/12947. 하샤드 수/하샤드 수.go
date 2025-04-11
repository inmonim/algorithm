import "strconv"

func solution(x int) bool {
    
    s := strconv.Itoa(x)
    sum := 0
    for _, v := range s {
        sum += int(v - '0')
    }
    
    if x % sum == 0 {
        return true
    }
    return false
}