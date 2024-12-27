def del_enem(people,enemies):
    res = []
    for enemy in enemies:
        for i in range (0,len(people)-1):
            if people[i] != enemy and people[i] not in res :
                res.append(people[i])

    return res

print(del_enem(['matt','alex','bob'], ['alex', 'bob']))