order = list(map(int, input().split()))
ascending = [1,2,3,4,5,6,7,8]
if order == ascending:
    print('ascending')
elif order == ascending[::-1]:
    print('descending')
else:
    print('mixed')