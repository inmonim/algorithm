func solution(n int) int {
    
    sum := 0
    
    for i := 1; i <= n; i++ {
        
        if n % i == 0 {
            sum += i
        }
    }
    return sum
}