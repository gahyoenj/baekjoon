def solution(my_string, overwrite_string, s):
    answer = ''
    n = len(overwrite_string)
    answer += my_string[:s]
    # print(answer)
    answer+= overwrite_string
    if len(answer) != len(my_string):
        answer += my_string[n+s::]
    return answer