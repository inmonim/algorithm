def solution(book_time):
    rooms = [[[0]]]
    am_book = []
    for time in book_time:
        time_set = [0, 0]
        for i in [0, 1]:
            h, m = time[i].split(':')
            am = int(h)*60 + int(m) + i*10
            time_set[i] = am
        am_book.append(time_set)
    
    am_book.sort(key=lambda x: x[0])
    print(am_book)
        
    rooms[0][0] = am_book[0]
    
    for time in am_book[1:]:
        new_room_count = len(rooms)
        
        for i in range(len(rooms)):
            room = rooms[i]
            can_in = 1
            
            for res in room:
                if time[1] <= res[0] or res[1] <= time[0]:
                    continue
                else:
                    new_room_count -= 1
                    can_in = 0
                    break
            if can_in:
                rooms[i].append(time)
                break

        if not new_room_count:
            rooms.append([time])
    print(rooms)

    return len(rooms)