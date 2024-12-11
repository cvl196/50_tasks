def doter (x,y):

    if len(x) != len(y):
        print('Неравное количество точек')
        return
    dots = []
    for i in range (len(x)):
        dots.append(f"({x[i]};{y[i]})")

    return dots

print(doter([5,34,234234,345325], [4324,23423455,43243,2]))