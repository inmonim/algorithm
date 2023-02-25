for t in range(int(input())):
    n =int(input())
    if (n%2==1):
        x=n//2+1
    else:
        x=-n//2
    print(f'#{t+1} {x}')