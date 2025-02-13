def solution(triangle):
    answer = 0
    height = len(triangle)-1
    while height > 0:
        for i in range(height):
            triangle[height-1][i] += max(triangle[height][i], triangle[height][i+1])
        height -= 1
    answer = triangle[0][0]
    return answer