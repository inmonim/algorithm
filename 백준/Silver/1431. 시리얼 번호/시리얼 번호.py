serial = [input().strip() for _ in range(int(input()))]
serial.sort(key=lambda x : (len(x), sum([int(i) for i in x if i.isdigit()]), x))
print(*serial, sep='\n')