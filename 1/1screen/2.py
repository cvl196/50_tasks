def change(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1], lst[0]
    return lst

print(change([124,436346,3464333]))