str = input()
new_str=''
for idx in range(len(str)):
    if str[idx].isupper() == True:
        new_str += str[idx].lower()
    elif str[idx].islower() == True:
        new_str += str[idx].upper()
print(new_str)