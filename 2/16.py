#Функция принимает массив массивов данных коробок

def sizer (data):

    full_size = []
    for i in data:
        size = 1
        for j in i:
            size *= j
        full_size.append(size)
    res = 0
    for i in full_size:
        res += i
    return res

print(sizer([[1,3,4],[2,2,2],[3,3,3]]))
