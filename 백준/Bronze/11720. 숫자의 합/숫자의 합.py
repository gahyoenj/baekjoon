N = int(input())
number = int(input())
number_str = list(str(number))
number_int = map(int,number_str)
print(sum(number_int))