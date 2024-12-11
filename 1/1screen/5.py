def lst_sort(lst):
    for i in range(len(lst)):
        for i in range (len(lst)-1):
            if lst[i]>lst[i+1]:
                lst [i],lst[i+1]=lst[i+1],lst[i]
    return lst

print(lst_sort([3,-34325,6366436,34666699999,43333,99999]))