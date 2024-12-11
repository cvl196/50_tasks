def search_substr(subst,st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        return ('Есть контакт')
    else:
        return ('Мимо')

search_substr('abc','ABCfc;fjasdfjasabf')
search_substr('abc','abasdfacfc;fjasdfjasabf')