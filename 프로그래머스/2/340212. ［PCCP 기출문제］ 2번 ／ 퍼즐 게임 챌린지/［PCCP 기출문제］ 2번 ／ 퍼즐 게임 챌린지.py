# def solution(diffs, times, limit):
#     answer = 0
#     right = max(diffs)
#     while answer < right:
#         mid = (answer + right) // 2
#         time_cur = 0
#         for i in range(len(diffs)):
#             if diffs[i] > mid:
#                 wrong = diffs[i] - mid
#                 if i-1>=0:
#                     time_cur += (times[i-1]+ times[i]) * wrong + times[i]
#                 elif i==0:
#                     time_cur += times[i] * wrong + times[i]
#             else:
#                 time_cur += times[i]
#         if time_cur > limit:
#             answer = mid + 1
#         else:
#             right = mid
#     return answer

def solution(diffs, times, limit):
    # 가능한 숙련도 범위 설정
    left, right = 1, max(diffs)
    
    # 이진 탐색 시작
    while left < right:
        mid = (left + right) // 2
        total_time = 0
        
        # 각 퍼즐을 순회하며 시간 계산
        for i in range(len(diffs)):
            if i == 0:
                time_prev = 0  # 첫 번째 퍼즐의 이전 시간은 0으로 초기화
            else:
                time_prev = times[i - 1]
                
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= mid:
                # 숙련도가 충분하면 틀리지 않고 푼다
                total_time += time_cur
            else:
                # 숙련도가 부족하면 틀린 만큼의 시간 계산
                wrong_attempts = diff - mid
                total_time += (time_cur + time_prev) * wrong_attempts + time_cur
                
            # 제한 시간 초과 시 중지
            if total_time > limit:
                break
        
        # 제한 시간 내에 가능한지에 따라 이진 탐색 범위 조정
        if total_time > limit:
            left = mid + 1
        else:
            right = mid
    
    return left
