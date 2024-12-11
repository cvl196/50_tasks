def reverser(a, b = []):
    length = len(a)
    for i in range(length - 1, -1, -1):
        b.append(a[i])
    return b

print(reverser([1, 2, 3, 4, 5]))