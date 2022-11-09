s = input()
c = '1 2 3 4 5 6 7 8'
if s == c:
    print('ascending')
elif s == c[::-1]:
    print('descending')
else:
    print('mixed')