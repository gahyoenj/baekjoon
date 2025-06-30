def solution(files):
    answer = []
    file_lst = []
    for idx in range(len(files)):
        file = files[idx]
        start = -1
        end = -1
        for i in range(len(file)):
            if file[i].isdigit():
                if start == -1:
                    start = i
                end = i
            elif start != -1:
                break
        
        head = file[:start]
        number = int(file[start:end+1])
        
        # print(head,number,tail)
        file_lst.append([head,number,file,idx])
    print(file_lst)
    file_lst.sort(key=lambda x: (x[0].lower(), x[1], x[3]))
    
    
    for idx in range(len(file_lst)):
        answer.append(file_lst[idx][2])
        
    return answer