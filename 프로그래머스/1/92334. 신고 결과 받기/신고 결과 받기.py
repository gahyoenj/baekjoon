def solution(id_list, report, k):
    answer = []
    complaint = {}
    mail = {}
    for user in id_list:
        complaint[user] =[] 
        mail[user] = 0
    report = set(report)
    
    for r in report:
        user_id, comp_id = r.split()
        complaint[comp_id].append(user_id)
        
    for user in id_list:
        if len(complaint[user]) >= k:
            for mail_id in complaint[user]:
                mail[mail_id] += 1
                
    for user in id_list:
        answer.append(mail[user])
    return answer