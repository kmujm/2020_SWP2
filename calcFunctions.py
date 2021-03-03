from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except SyntaxError as se:
        return se
    except ValueError as ve:
        return ve
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except SyntaxError as se:
        return se
    except TypeError as te:
        return te
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except ValueError  as ve:
        return ve
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    if n >= 4000:
        return 'Error!'



    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def romanToDec(numStr):
    n = 0
    i = 0
    for value, letters in romans:
        while numStr.find(letters) == i:
            n += value
            numStr = numStr[len(letters):]
    return n

romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')]

constantFunction = [('pi', '3.141592'),
                    ('빛의 이동 속도 (m/s)', '3E+8'),
                    ('소리의 이동 속도 (m/s)', '340'),
                    ('태양과의 평균 거리 (km)', '1.5E+8')]
#상수는 문장의 처음, 연산자 다음에만 입력 가능 상수 뒤에는 연산자만 입력이 가능 

functionMap = [
    ('factorial (!)', factorial),
    ('-> binary', decToBin),
    ('binary -> dec', binToDec),
    ('-> roman', decToRoman),
    ('roman -> dec', romanToDec),
]
