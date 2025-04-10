func solution(x int, n int) []int64 {
    
    x1 := int64(x)
    
    arr := []int64{x1}
    
    for i := 1; i < n; i ++ {
        x1 += int64(x)
        arr = append(arr, x1)
    }
    
    return arr
    
}