def solution(new_id):
    answer = ''
    one = ''
    for char in new_id:
        if char.isupper():
            one += char.lower()
        else:
            one += char
    two = ''
    for char in one:
        if char.isdigit() or char.isalpha() or char in ['-','_','.']:
            two += char
    
    three = ''
    for char in two:
        if len(three) and three[-1] == '.' and char=='.':
            continue
        three += char
    if three and three[0] == '.':
        three = three[1:]
    if three and three[-1] == '.':
        three = three[:-1]
    
    if not three:
        three = 'a'
    
    if len(three) >= 16:
        three = three[:15]
    if three and three[-1] == '.':
        three = three[:-1]
    
    if len(three) <= 2:
        new = three[-1]
        while len(three) < 3:
            three += new
    answer = three
    
    
    return answer