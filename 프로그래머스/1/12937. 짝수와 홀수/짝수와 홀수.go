func solution(num int) string {
    answer := ""
    if num % 2 == 0 {
        answer = "Even"
    } else {
        answer = "Odd"
    }
    return answer
}