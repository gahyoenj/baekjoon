def solution(players, callings):
    answer = []
    rank = {}
    for idx,player in enumerate(players):
        rank[player] = idx
    for call in callings:
        idx = rank[call]

        over = players[idx-1]
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        rank[call] -= 1
        rank[over] += 1
        
    return players