def fibo(n):
  fibo_list = [1,1]
  for i in range(2, n):
    fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
  return fibo_list[-1]



def fibonacci(n):
  fibonacci_cnt = 0
  fibo_list = [1,1]
  for i in range(2, n):
    fibonacci_cnt += 1
    fibo_list.append(fibo_list[i-2]+fibo_list[i-1]) 
  return fibonacci_cnt

n = int(input())
print(fibo(n), fibonacci(n))