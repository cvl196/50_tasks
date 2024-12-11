def lucky_ticket(n):
    n = n/2
    n = int(n)
    sum = 0
    for i in range (0,10**n):
        for j in range (0,10**n):
            if i == j and i != 0:
                sum += 1
    return sum

print(lucky_ticket(6))