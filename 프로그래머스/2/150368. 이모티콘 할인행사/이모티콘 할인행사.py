from itertools import product
def solution(users, emoticons):
    answer = []
    rate = [10,20,30,40]
    
    result = []
    for arr in product(rate,repeat=len(emoticons)):
        purchase = 0
        service = 0
        for user in users:
            sumV = 0
            for idx in range(len(emoticons)):
                if user[0] <= arr[idx]:
                    sumV += (emoticons[idx] * ((100-arr[idx])/100))
            if int(sumV) >= user[1]:
                service += 1
            else:
                purchase += int(sumV)
        result.append((service, purchase))
    
    result.sort(key=lambda x:(x[0],x[1]),reverse = True)
    answer = result[0]
    return answer