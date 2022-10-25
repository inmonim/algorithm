i=input()
while i:
    if i == i[::-1]:
        print('yes')
    else:
        print('no')
    i=input()
    if i == '0':
        break