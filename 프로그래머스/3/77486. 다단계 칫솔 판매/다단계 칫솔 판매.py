def solution(enroll, referral, seller, amount):
    answer = []
    ref = {'center':''}
    result = {'center':0}
    

    for name in enroll:
        ref[name] = ''
        result[name] = 0
    
    for idx in range(len(referral)):
        if referral[idx] == '-':
            ref[enroll[idx]] = 'center'
            continue
        
        ref[enroll[idx]] = referral[idx]
    
    # print(ref)
    
    for idx in range(len(seller)):
        s = seller[idx]
        money = amount[idx] * 100
        
        
        recommender = s
        
        
        while recommender and money > 0:
            give = money // 10
            get = money - give
            
            result[recommender] += get
            recommender = ref[recommender]
            
            money = give
    
    for person in enroll:
        answer.append(result[person])
    
    return answer