def solution(arr):
    answer = []
    cnt = {0:0, 1:0}
    st = [(0, 0, len(arr))]

    while st:
        row, col, size = st.pop()
        num = arr[row][col]
        same = True

        for i in range(row, row + size):
            for j in range(col, col + size):
                if arr[i][j] != num:
                    same = False
                    break
            if not same:
                break

        if same:
            cnt[num] += 1
        else:
            half = size // 2
            st.append((row,col,half))
            st.append((row,col+half,half))
            st.append((row+half,col,half))
            st.append((row+half,col+half,half))
            
    
    for n in cnt.values():
        answer.append(n)
    return answer