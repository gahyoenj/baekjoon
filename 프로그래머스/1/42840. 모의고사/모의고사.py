def solution(answers):
    answer = []
    score = {}
    A = [i for i in range(1,6)]
    scoreA = 0
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scoreB, scoreC = 0, 0
    for idx in range(len(answers)):
        if answers[idx] == A[idx % len(A)]:
            scoreA += 1
        if answers[idx] == B[idx % len(B)]:
            scoreB += 1
        if answers[idx] == C[idx % len(C)]:
            scoreC += 1

    score[1] = scoreA
    score[2] = scoreB
    score[3] = scoreC
    maxV = max(score.values())
    print(maxV)
    for idx in range(1,4):
        if score[idx] == maxV:
            answer.append(idx)
    return answer