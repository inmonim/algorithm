def solution(plans):

    def parsing_time(s):
        h, m = s.split(':')
        x = int(m) + int(h)*60
        return x
    
    for i in range(len(plans)):
        plan = plans[i]
        plans[i] = [plan[0], parsing_time(plan[1]), int(plan[2])]
    plans.sort(key=lambda x:x[1])
    
    answer = []
    stack = []
    
    while plans:
        
        plan = plans.pop(0)
        
        if not plans:
            answer.append(plan[0])
            break
        
        next_plan = plans[0]
        plan_end = plan[1] + plan[2]
        
        if plan_end == next_plan[1]:
            answer.append(plan[0])
        elif plan_end > next_plan[1]:
            remain_time = plan_end - next_plan[1]
            stack.append([plan[0], remain_time])
        else:
            gap_time = next_plan[1] - plan_end
            answer.append(plan[0])
            
            while gap_time and stack:
                gap_plan = stack.pop()
                if gap_time >= gap_plan[1]:
                    answer.append(gap_plan[0])
                    gap_time -= gap_plan[1]
                else:
                    stack.append([gap_plan[0], gap_plan[1] - gap_time])
                    break
    
    for _ in range(len(stack)):
        answer.append(stack.pop()[0])
    
    return answer