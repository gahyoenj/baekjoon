def solution(jobs):
    answer = 0
    n = len(jobs)
    wait = []
    
    current = 0
    total = 0
    while jobs or runnable:
        runnable = []
        for job in jobs:
            if job[0] <= current:
                runnable.append(job)
                
        if runnable:
            runnable.sort(key= lambda x: x[1])
            
            current_job = runnable[0]
            jobs.remove(current_job)
            # jobs.pop(0)
            
            current += current_job[1]
            total += (current - current_job[0])
        else:
            current += 1
    answer = total // n
    return answer