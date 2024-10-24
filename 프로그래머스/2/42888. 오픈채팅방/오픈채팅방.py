def solution(record):
    answer = []
    dic = {}
    
    # 모든 기록을 순회하며 최종 닉네임을 저장
    for str in record:
        command = str.split(' ')
        if command[0] == 'Enter' or command[0] == 'Change':
            user_id = command[1]
            nickname = command[2]
            dic[user_id] = nickname
    
    # 기록을 순회하며 결과 메시지를 작성
    for user in record:
        command = user.split(' ')
        action = command[0]
        user_id = command[1]
        
        if action == 'Enter':
            answer.append(f"{dic[user_id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f"{dic[user_id]}님이 나갔습니다.")
    
    return answer
