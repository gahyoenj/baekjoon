def solution(n, w, num):
    answer = 1
    number = [i for i in range(1,n+1)]
    box = []
    flag = 1
    for i in range(0,n+1,w):
        if flag == -1 and len(number[i:i+w]) < w:
            numbers = [0] * (w -len(number[i:i+w])) + number[i:i+w][::-1]
            box.append(numbers)
        elif flag == 1:
            box.append(number[i:i+w])
        else:
            box.append(number[i:i+w][::-1])
        flag *= -1
    idx = -1
    for i in range(len(box)):
        if idx >= 0 and idx < len(box[i]) and box[i][idx] > 0:
            answer += 1
        if num in box[i]:
            idx = box[i].index(num)
                  
    return answer