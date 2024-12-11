def encoder (st):
    st.lower()
    word = ''
    for i in st:
        print(i)
        if i == "е":
            word += "3"
        elif i == "а":
            word += "4"
        else:
            word += i
    return word

print(encoder('привет как дела'))