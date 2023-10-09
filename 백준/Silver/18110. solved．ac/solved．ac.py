import sys

def rounds(num):
    first_demical_place = num - int(num)

    if first_demical_place // 0.5:
        num = int(num)+1
    else:
        num = int(num)
    
    return num

N = int(input())

level_list = sorted([int(sys.stdin.readline()) for _ in range(N)])

if level_list:

    per15 = rounds(N * 0.15)

    level_list = level_list[per15:len(level_list)-per15]

    avg = sum(level_list)/len(level_list)

    result = rounds(avg)
else:
    result = 0
    
print(result)