def solution(num_list):
    multiple = 1
    for idx in range(len(num_list)):
        multiple *= num_list[idx]
    if multiple > sum(num_list) ** 2:
        return 0
    elif multiple < sum(num_list) ** 2:
        return 1