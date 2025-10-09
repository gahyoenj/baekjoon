def solution(ingredient):
    answer = 0
    st = []
    hamburger = [1,2,3,1]
    for idx in range(len(ingredient)):
        st.append(ingredient[idx])
        if len(st) >= 4:
            if st[-4:] == hamburger:
                answer += 1
                for i in range(4):
                    st.pop()
        
    return answer