import re

def solution(id):
    id = id.lower()
    id = re.sub('[^a-z0-9._-]','',id)
    while '..' in id:
        id = id.replace('..', '.')
    if id[0] == '.':
        id = id[1:]
    if id == '':
        id = 'a'
        
    id = id[:15]
    if id[-1] == '.':
        id = id[:-1]
    while len(id) < 3:
        id += id[-1]
    if id[-1] == '.':
        id = id[:-1]
        
    return id