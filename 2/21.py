def mid (numbers):
    if len(numbers)%2 == 0:
        return 'Требуется нечетное количество чисел'
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]


    return numbers[len(numbers)//2]

print(mid([324,23423432,35345,3553,32]))