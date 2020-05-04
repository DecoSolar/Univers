import EK_for_DH
import numpy as np

def Vibor(k):#k - порядок ЭК
    j = 0
    while j == 0:
        a = int(input("Введите число не превышающее порядок ЭК: "))
        if a > k:
            print("Попробуйте еще раз.")
        else:
            return a

def Peredacha(c, B, p, a):
    return EK_for_DH.Umnozenie(B, c, p, a)

def Key(c, B, p, a):
    return EK_for_DH.Umnozenie(B, c, p, a)

if __name__ == '__main__':
    j = 0
    while j == 0:
        k = int(input("1 - выбор поля и ЭК\n2 - выбрать открытый ключ\n3 - выбрать закрытый ключ первого абонента\n4 - выбрать закрытый ключ второго абонента\n5 - получить секретный ключ\n6 - выход\n"))
        if k == 1:#выбор поля и ЭК
            p = EK_for_DH.Proverka()
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            pole1 = EK_for_DH.NahozTochek(a, b, p)
            pole = pole1[0]
            kolvo = pole1[1]
            if np.all(pole) == True:
                print("Try again")
        elif k == 2:#выбрать открытый ключ
            if 'pole' in locals():
                B = EK_for_DH.VvodTochek(pole)
            else:
                print("Сначала выберете поле.")
        elif k == 3:#выбор закрытого ключа Алисы
            if 'kolvo' in locals():
                A = Vibor(kolvo)
            else:
                print("Сначала выберете поле.")
        elif k == 4:#выбор закрытого ключа Боба
            if 'kolvo' in locals():
                b = Vibor(kolvo)
            else:
                print("Сначала выберете поле.")
        elif k == 5:#Получение секретного ключа, мб в файл
            if 'pole' in locals() and 'kolvo' in locals() and 'b' in locals() and 'A' in locals() and 'B' in locals():
                oft = Peredacha(A, B, p, a)#от А -> В, точка
                tfo = Peredacha(b, B, p, a)#от В -> А, точка
                secret = Key(A, tfo, p, a)
                secret2 = Key(b, oft, p, a)
                if secret == secret2:
                    print("Все прошло удачно. Ваш секретный ключ: ", secret)
                else:
                    print("Что-то пошло не так. Попробуйте еще раз.")
            else:
                print("Введите остальные данные, чтобы продолжить.")
        elif k == 6:#выход
            j = 1
        else:
            print("ERROR")
