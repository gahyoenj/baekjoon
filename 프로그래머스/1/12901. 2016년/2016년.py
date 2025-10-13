def solution(a, b):
    answer = ''
    
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    days = sum(month[:a-1]) + b-1
    current = 5
    answer = week[(current + days) % 7]
    return answer