def time24_to_12 (time):
    hours = ''
    minutes = ''
    for i in range (0,2):
        hours += time[i]
    for i in range(3, 5):
        minutes += time[i]

    hours = int(hours)
    if hours > 12:
        hours = hours - 12
    else:
        hours = hours
    res = str(hours) + ':' + str(minutes)
    return res
def time12_to_24 (time, pm):
    hours = ''
    minutes = ''
    for i in range (0,2):
        hours += time[i]
    for i in range(3, 5):
        minutes += time[i]

    if pm:
        hours = int(hours) +12

    res = str(hours) + ':' + str(minutes)
    return res
#   Функиця timer принимает первым аргументом время в формате 12:23, вторым аргументом формат исходного времени,
# в случае перевода из 12 часовой системы третьим параметром передается true если время pm
def timer (st, type, pm = None):
    if type == '12':
        res = time12_to_24(st, pm)
    elif type == '24':
        res = time24_to_12(st)
    return res
print(timer('13:43', '24', pm = False))