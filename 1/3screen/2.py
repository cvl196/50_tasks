def help_bool(a):
    info = {
        'к': 'Коммутативность (переместительность) — свойство сложения и умножения чисел, выражаемое тождествами: а+b=b+a, ab =ba. ',
        'а': 'Ассоциативность — свойство операций сложения и умножения чисел, выражаемое тождествами: (а + b) + c = a + (b + c) и (ab)c = a(bc). ',
        'д': 'Дистрибутивность (от лат. distributivus — распределительный) — свойство умножения, выражаемое тождествами: с (a + b) = са + cb и (а + b)c = ас + bc. ',
        'м': 'Законы де Мо́ргана (правила де Мо́ргана) — логические правила, связывающие пары логических операций при помощи логического отрицания. Названы в честь шотландского математика Огастеса де Моргана',
    }
    curinfo = info[a]
    if curinfo:
        return curinfo
    else: 
        return 'Выберете букву к, а , д, м'


print(help_bool('м'))