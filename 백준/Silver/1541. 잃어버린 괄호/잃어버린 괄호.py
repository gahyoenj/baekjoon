exp = input()

if '-' in exp:
    formula = exp.split("-")

    lst = []
    # print(formula)
    for idx in range(len(formula)):
        if "+" in formula[idx]:
            ans = 0
            str = formula[idx].split("+")
            for num in str:
                ans -= int(num)
            lst.append(ans)
        else:
                lst.append(-int(formula[idx]))

    if lst[0] < 0:
        lst[0] = -lst[0]
    print(sum(lst))

else:
    ans = 0
    formula = exp.split("+")
    for num in formula:
        ans += int(num)
    print(ans)