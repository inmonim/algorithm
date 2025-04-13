func solution(schedules []int, timelogs [][]int, startday int) int {
    
    answer := 0
    
    for i := 0; i < len(schedules); i++ {
        answer += isPresent(schedules[i], timelogs[i], startday)
    }
    
    return answer
}

func isPresent(schedule int, timelog []int, date int) int {
    
    if schedule % 100 >= 50 {
        schedule += 50
    } else {
        schedule += 10
    }
    
    for _, v := range timelog {
        if date > 5 {
            if date == 6 {
                date = 7
            } else {
                date = 1
            }
            continue
        }
        
        if v > schedule {
            return 0
        }
        date ++
    }
    return 1
}