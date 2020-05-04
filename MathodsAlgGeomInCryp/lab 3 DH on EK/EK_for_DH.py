import numpy as np

def Slozenie(x1, y1, x2, y2, p):
    znam = x2 - x1
    chisl = y2 - y1
    if znam == 0:
        return 'точка на бесконечности'
    elif znam < 0:
        znam = -znam
        chisl = -chisl
    x = (chisl / znam) % p
    if (x).is_integer() == True:
        x3 = (x**2 - ((x1 + x2) % p)) % p
        y3 = (x * ((x1 - x3) % p) - y1) % p
    else:
        for i in range(2, int(znam)):
            if znam % i == 0 and p % i == 0:
                return 1    #Возвращаем 1 если НОД не равен единице
        znam = znam % p
        znam = Obratnoe(p, znam)
        chisl = chisl % p
        mnoz = (znam * chisl) % p
        x3 = ((mnoz)**2 - ((x1 + x2) % p)) % p
        y3 = (mnoz * ((x1 - x3) % p) - y1) % p
    return x3, y3

def Umnozenie(tochka, k, p, a):
    x = tochka[0]
    y = tochka[1]
    x3 = 0
    y3 = 0
    for i in range(2, k+1):
        if i == 2 or (x3 == x and y3 == y):
            znam = 2 * y
            chisl = 3 * x**2 + a
            x1 = (chisl / znam) % p
            if (x1).is_integer() == True:
                x3 = int((x1**2 - 2 * x) % p)
                y3 = int((x1 * ((x - x3) % p) - y) % p)
            else:
                znam = znam % p
                znam = Obratnoe(p, znam)
                chisl = chisl % p
                mnoz = (chisl * znam) % p
                x3 = int((mnoz**2 - 2 * x) % p)
                y3 = int((mnoz * ((x - x3) % p) - y) % p)
        else:
            summa = Slozenie(x3, y3, x, y, p)
            x3 = int(summa[0])
            y3 = int(summa[1])
    return x3, y3



def Diskrim(a, b, p):   #chek
    return (4 * a**3 + 27 * b**2) % p

def Proverka():         #chek
    i = 2
    j = 1
    while j == 1:
        p = int(input('Введите число p(поле): '))
        while i < p:
            if p % i == 0:
                print('Число, которое вы ввели, должно быть простым.')
                break
            else:
                i += 1
        if i == p:
            j = 0
    return p


def Obratnoe(p, x):
    for i in range(p):
        if (x * i) % p == 1:
            a = i
            return a


def NahozTochek(a, b, p):
    D = Diskrim(a, b, p)
    if D == 0:
        print("Дискриминант равен 0. Функция не взаимно проста с ее производной, а значит такая кривая не является ЭК.")
        return -1, -1
    else:
        n = p * 2
        mass = np.zeros((n, 2))
        i = 0
        k = 1
        for x in range(p):
            z = (x**3 + a * x + b) % p
            try:
                y1, y2 = [y for y in range(p) if y*y % p == z]       
                l = x*x % p
                k += 2
                mass[i][0] = x
                mass[i][1] = y1
                i += 1
                mass[i][0] = x
                mass[i][1] = y2
                i += 1
                print('x =', x, 'x^2 =', l, 'y^2 =', z, 'y =', y1, y2, sep = '\t')
            except ValueError:
                try:
                    y = [y for y in range(p) if y*y % p == z]       
                    l = x*x % p
                    mass[i][0] = x
                    if y == [0]:
                        mass[i][1] = 0
                        k += 1
                        i += 1
                        print('x =', x, 'x^2 =', l, 'y^2 =', z, 'y =', 0, sep = '\t')
                except ValueError:
                    k = k
            except DeprecationWarning:
                k = k
        if b == 0:
            k += 1
        print("#E", p, "(", a, ",", b, ") =", k)
        return mass, k


def VvodTochek(mass):
    j = 0
    while j == 0:
        x, y = map(int, input("Введите координаты точки через пробел: ").split())
        mass1 = np.array([x, y])
        k = 0
        l = len(mass)
        for i in range(l):
            if np.all(mass[i] == mass1) == True:
                k = 1
        if k == 0:
            print("Этой точки не существует. Попробуйте еще раз.")
        elif k == 1:
            return x, y
    


if __name__ == '__main__':
    j = 0
    while j == 0:
        k = int(input("1 - нахождение точек ЭК\n2 - сложение точек\n3 - умножение точки на число\n4 - выход\n"))
        if k == 1:      #нахождение точек
            p = Proverka()
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            D = Diskrim(a, b, p)
            if D == 0:
                print("Дискриминант равен 0. Функция не взаимно проста с ее производной, а значит такая кривая не является ЭК.")
            else:
                print("Уравнение эллиптической кривой: y^2 = (x^3 + %s * x + %s) mod %s" % (a, b, p))
                tochki = NahozTochek(a, b, p)
        elif k == 2:    #сложение точек
            if 'tochki' in locals():
                x1, y1 = VvodTochek(tochki)
                x2, y2 = VvodTochek(tochki)
                summa = Slozenie(x1, y1, x2, y2, p)
                if summa == 1:
                    print("НОД равен 1. Нельзя найти обратное, вычисление невозможно.")
                elif summa == "точка на бесконечности":
                    print("(", x1, ",", y1, ") + (", x2, ",", y2, ") = точка на бесконечности")
                else:
                    print("(", x1, ",", y1, ") + (", x2, ",", y2, ") = (", summa[0], ",", summa[1], ")")
            else:
                print("Найдите сначала точки.")
        elif k == 3:    #умножение точек
            if 'tochki' in locals():
                x1, y1 = VvodTochek(tochki)
                l = int(input("Введите число, на которую нужно умножить точку: "))
                proizv = Umnozenie(x1, y1, l, p, a)
                if proizv == ('т', 'о'):
                    print(l, " * (", x1, ",", y1, ") = точка на бесконечности")
                else:
                    print(l, " * (", x1, ",", y1, ") = (", proizv[0], ",", proizv[1], ")")
            else:
                print("Найдите сначала точки.")
        elif k == 4:    #выход
            j = 1
        else:           #введено не верное число
            print("ERORR")



