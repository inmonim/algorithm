def solution(wallpaper):
    x_, y_ = [], []
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                x_.append(x)
                y_.append(y)
    
    answer = [min(y_), min(x_), max(y_)+1, max(x_)+1]
    return answer