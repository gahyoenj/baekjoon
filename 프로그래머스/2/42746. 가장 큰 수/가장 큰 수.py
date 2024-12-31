def solution(numbers):
    answer = ''
    for idx in range(len(numbers)):
        numbers[idx] = str(numbers[idx])
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return answer if answer[0] != '0' else '0'