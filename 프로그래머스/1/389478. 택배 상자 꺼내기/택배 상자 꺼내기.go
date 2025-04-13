// import "fmt"

func solution(n int, w int, num int) int {
    
    var boxMat [][]int
    
    refeat := n/w
    
    if n%w != 0 {
        refeat += 1
    }
    
    left := true
    min := 1
    for i := 0; i < refeat; i++ {
        tmpList := make([]int, w)
        if left {
            for i := 0; i < w; i++ {
                tmpList[i] = min
                min++
            }
            left = false
        } else {
            for i := w-1; i >= 0; i-- {
                tmpList[i] = min
                min++
            }
            left = true
        }
        boxMat = append(boxMat, tmpList)
    }
    
    answer := 1
    
    tx := 0
    plag := false
    for y := 0; y < refeat; y++ {
        
        for x := 0; x < w; x++ {
            
            if plag && x == tx && boxMat[y][x] <= n {
                answer += 1
            }
            
            if boxMat[y][x] == num {
                tx = x
                plag = true
            }
        }
    }
    
    return answer
}