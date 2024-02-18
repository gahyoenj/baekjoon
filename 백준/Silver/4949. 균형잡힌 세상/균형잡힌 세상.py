while True:
    s = input()
    if s == '.':
        break
    st = []
    for c in s:
        if c == '(' or c == '[':
            st.append(c)
        elif c == ')':
            if not st or st.pop() != '(':
                print("no")
                break
        elif c == ']':
            if not st or st.pop() != '[':
                print("no")
                break
    else:
        if st:
            print("no")
        else:
            print("yes")