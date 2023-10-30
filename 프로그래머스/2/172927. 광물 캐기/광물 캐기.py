def solution(picks, minerals):
    answer = 0
    stone = {'diamond':25, 'iron':5, 'stone':1}
    iron = {'diamond':5, 'iron':1, 'stone':1}
    
    minerals = minerals[:sum(picks)*5]
    
    dia_pick_list = []
    iron_pick_list = []
    stone_pick_list = []
    pick_list = [dia_pick_list, iron_pick_list, stone_pick_list]
    
    for i in range(len(minerals)//5 + 1):
        dia_pick_list.append(len(minerals[i*5 : i*5+5]))
        iron_pick_list.append(sum([iron[j] for j in minerals[i*5: i*5 + 5]]))
        stone_pick_list.append(sum([stone[j] for j in minerals[i*5: i*5 + 5]]))
    
    if dia_pick_list[-1] == 0:
        for l in pick_list:
            l.pop()
    
    for pick_index in range(3):
        for _ in range(picks[pick_index]):

            if not stone_pick_list:
                break
            i = stone_pick_list.index(max(stone_pick_list))
            
            for j in range(3):
                if j == pick_index:
                    answer += pick_list[j].pop(i)
                else:
                    pick_list[j].pop(i)
    
    return answer