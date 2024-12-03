def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    p = int(pos.replace(':', ""))
    start = int(op_start.replace(":", ""))
    end = int(op_end.replace(":", ""))
    
    # 처음에 오프닝 구간 체크
    if start <= p <= end:
        pos = op_end

    for do in commands:
        hour, minute = map(int, pos.split(':'))
        if do == 'next':
            minute += 10
            if minute >= 60:
                minute -= 60
                hour += 1

            # 동영상 끝을 초과하면 마지막 위치로 고정
            if hour * 60 + minute > int(video_len[0:2]) * 60 + int(video_len[3:]):
                hour = int(video_len[0:2])
                minute = int(video_len[3:])
        else:  # 'prev'
            minute -= 10
            if minute < 0:
                minute += 60
                hour -= 1

            # 동영상 시작보다 작아지면 처음 위치로 고정
            if hour < 0:
                hour = 0
                minute = 0

        # 시간 포맷 재조합
        pos = f"{hour:02}:{minute:02}"

        # 명령 수행 후 오프닝 구간 체크
        p = int(pos.replace(":", ""))
        if start <= p <= end:
            pos = op_end

    answer = pos
    return answer
