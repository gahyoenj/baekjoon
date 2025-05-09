def solution(want, number, discount):
    answer = 0
    want_product = []
    for idx in range(len(number)):
        for _ in range(number[idx]):
            want_product.append(want[idx])

    want_product.sort()
    
    for i in range(len(discount)-9):
        buy = []
        for product in discount[i:i+10]:
            if product in want:
                buy.append(product)
        buy.sort()
        if buy == want_product:
            answer += 1
    return answer