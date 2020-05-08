import EK_for_MO
import numpy as np
import math

def NOD(N): #ввод числа и находим наименьший общий делитель и если он не равен 1, то ввод еще раз
    j = 0
    while j == 0:
        e = int(input("Введите числе не больше N = #Ep(a,b) и взаимнопростое с N: "))
        if e > N or math.gcd(e, N) != 1:#gcd находит НОД
            print("Try again")
        else:
            d = EK_for_MO.Obratnoe(N, e)
            return e, d

def Encryp(A, B, e, pm, p, a): #шифруем сообщение
    M = EK_for_MO.Umnozenie(pm, e, p, a)
    print(A, "передает", B, ":", M)
    return M

def Decryp(d, m, p, a): #расшифровуем
    M = EK_for_MO.Umnozenie(m, d, p, a)
    return M

if __name__ == '__main__':
    j = 0
    while j == 0:
        k = int(input("1 - ввести данные ЭК\n2 - ввести закрытые ключи отправителя\n3 - ввести закрытые ключи получателя\n4 - зашифровать сообщение\n5 - расшифровать зашифрованное сообщение\n6 - расшифровать любое сообщение\n7 - выход\n"))
        if k == 1:#ввод ЭК
            p = EK_for_MO.Proverka()
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            pole1 = EK_for_MO.NahozTochek(a, b, p)
            pole = pole1[0]
            N = pole1[1]
            if np.all(pole) == True:
                print("Try again")
        elif k == 2:#закрытые ключи отправителя
            if 'N' in locals():
                dan = NOD(N)
                ea = dan[0]
                da = dan[1]
            else:
                print("Введите сначала данные ЭК.")
        elif k == 3:#закрытые ключи получателя
            if 'N' in locals():
                dan = NOD(N)
                eb = dan[0]
                db = dan[1]
            else:
                print("Введите сначала данные ЭК.")
        elif k == 4:#зашифровать сообщение
            if 'ea' in locals() and 'eb' in locals():
                Pm = EK_for_MO.VvodTochek(pole)
                M = Encryp('A', 'B', ea, Pm, p, a)
                M = Encryp('B', 'A', eb, M, p, a)
                M = Encryp('A', 'B', da, M, p, a)
                print("Зашифрованный текст передан.")
            else:
                print("Найдите сначала закрытые ключи.")
        elif k == 5:#расшифровать зашифрованное
            if 'M' in locals():
                print("Расшифрованное сообщение:", Decryp(db, M, p, a))
            else:
                print("Сначала зашифруйте сообщение.")
        elif k == 6:#расшифровать любое
            if 'pole' in locals():
                db = int(input("Введите секретный ключ получателя: "))
                db = EK_for_MO.Obratnoe(N, db)
                M = EK_for_MO.VvodTochek(pole)
                print("Расшифрованное сообщение:", Decryp(db, M, p, a))
            else:
                print("Введите сначала поле.")
        elif k == 7:#выход
            j = 1
        else:
            print("ERROR")
