def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for i in range(len(phone_book) - 1):
        a, b = phone_book[i:i+2]
        l = min([len(a), len(b)])
        if a[:l] == b[:l]:
            answer = False
            break
    
    return answer