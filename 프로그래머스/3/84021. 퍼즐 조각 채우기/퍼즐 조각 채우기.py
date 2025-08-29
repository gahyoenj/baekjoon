def solution(game_board, table):
    
    def dfs(row,col,visited_arr,m,t,num):
        st = [(row,col)]
        p = []
        visited_arr[row][col] = True
        while st:
            nr,nc = st.pop(0)
            p.append((nr,nc))
            
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                newR = dr + nr
                newC = dc + nc
            
                if 0<=newR<m and 0<=newC<m and not visited_arr[newR][newC] and t[newR][newC] == num:
                    st.append((newR,newC))
                    visited_arr[newR][newC] = True
        return p
    
    def check(p,e):
        p_rot = p[:]
        
        e.sort()
        
        for i in range(4):
            
            if i != 0:
                rotate = []
                for pr,pc in p_rot:
                    rotate.append((pc,-pr))
                p_rot = rotate
        
            p_rot.sort()
            
            
            r = p_rot[0][0]
            c = p_rot[0][1]

            row = e[0][0]
            col = e[0][1]

            np = []
            ne = []

            for pr,pc in p_rot:
                pr -= r
                pc -= c
                np.append((pr,pc))

            for er,ec in e:
                er -= row
                ec -= col
                ne.append((er,ec))
            

            if np == ne:
                return True
            

    answer = 0
    puzzle = []
    puzzle_visited = [[False]* len(table) for _ in range(len(table))]
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row][col] == 1 and not puzzle_visited[row][col]:
                result = dfs(row,col,puzzle_visited,len(table),table,1)
                puzzle.append(result)
    # print(puzzle)
    
    visited =  [[False] * len(game_board) for _ in range(len(game_board))]
    empty = []
    
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] == 0 and not visited[row][col]:
                result = dfs(row,col,visited,len(game_board),game_board,0)
                empty.append(result)
    
    # print(empty)
    
    
    for pi in range(len(puzzle)-1, -1, -1):
        for ei in range(len(empty)-1, -1, -1):
            if len(puzzle[pi]) == len(empty[ei]):
                if check(puzzle[pi], empty[ei]):
                    answer += len(puzzle[pi])
                    puzzle.pop(pi)
                    empty.pop(ei)
                    break


    return answer