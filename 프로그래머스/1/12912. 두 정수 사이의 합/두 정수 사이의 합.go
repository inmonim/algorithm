func solution(a int, b int) int {
    s := 0
    e := 0
    if a <= b {
        s = a
        e = b
    } else {
        e = a
        s = b
    }
    
    sum := 0
    
    for s <= e {
        sum += s
        s++
    }
    
    return int(sum)
}