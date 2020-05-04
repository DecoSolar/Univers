import EK_for_EG_2
import numpy as np


symvoli = (' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~','А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
kodirovka = [[33,355],[33,396],[34,74],[34,677],[36,87],[36,664],[39,171],[39,580],[43,224],[43,527],[44,366],[44,385],[45,31],[45,720],[47,349],[47,402],[48,49],[48,702],[49,183],[49,568],[53,277],[53,474],[58,139],[58,612],[56,332],[56,419],[59,365],[59,386],[61,129],[61,622],[62,372],[62,379],[66,199],[66,552],[67,84],[67,667],[69,241],[69,510],[70,195],[70,559],[72,254],[72,497],[73,72],[73,679],[74,170],[74,581],[75,318],[75,433],[78,271],[78,480],[79,111],[79,640],[80,318],[80,433],[82,270],[82,481],[83,373],[83,378],[85,35],[85,716],[86,25],[86,726],[90,21],[90,730],[93,267],[93,484],[98,338],[98,413],[99,295],[99,456],[100,364],[100,387],[102,267],[102,484],[105,369],[105,382],[106,24],[106,727],[108,247],[108,504],[109,200],[109,551],[110,129],[110,622],[114,144],[114,607],[115,242],[115,509],[116,92],[116,659],[120,147],[120,604],[125,292],[125,249],[126,33],[189,297],[189,454],[192,32],[192,719],[194,205],[194,546],[197,145],[197,606],[198,224],[198,527],[200,30],[200,721],[203,324],[203,427],[205,372],[205,379],[206,106],[206,645],[209,82],[209,669],[210,31],[210,720],[215,247],[215,504],[218,150],[218,601],[221,138],[221,613],[226,9],[226,742],[227,299],[227,452],[228,271],[228,480],[229,151],[229,600],[234,164],[234,587],[235,19],[235,732],[236,39],[236,712],[237,297],[237,454],[238,175],[238,576],[240,309],[240,442],[243,87],[243,664], [247,266],[247,485],[249,183],[249,568],[250,14],[250,737],[251,245],[251,506],[253,211],[253,540],[256,121],[256,630],[257,293],[257,458]]


def Preobrazovanie(txt, mass, sym, kod):
    for i in range(len(mass)):
        j = sym.index(txt[i])#для 4 пункта должно быть list
        mass[i] = kod[j]
    return mass

def Preobrazovanie2(txt, mass, sym, kod):
    for i in range(len(mass)):
        j = sym.index(list(txt[i]))
        mass[i] = kod[j]
    return mass

def Encryption(Pm, k, eC, p, a):#шифруем
    M = EK_for_EG_2.Umnozenie(eC, k, p, a)
    M = EK_for_EG_2.Slozenie(Pm[0], Pm[1], M[0], M[1], p)
    return M

def Decryption(M, kC, e, p, a, pole):#расшифруем
    ekC = EK_for_EG_2.Umnozenie(kC, e, p, a)
    C = ObratnaiaToch(pole, ekC) 
    return EK_for_EG_2.Slozenie(M[0], M[1], C[0], C[1], p)

def ObratnaiaToch(pole, tochka):
    l = len(pole)
    
    for i in range(l):
        if np.all(pole[i] == tochka) == True:
            if pole[i-1][0] == tochka[0]:
                tochka = pole[i-1]
                return tochka
            elif pole[i+1][0] == tochka[0]:
                tochka = pole[i+1]
                return tochka

def OpenKeyB(e, C, p, a):
    return EK_for_EG_2.Umnozenie(C, e, p, a)

if __name__ == '__main__':
    j = 0
    while j == 0:
        p = 751
        a = -1
        b = 1
        print("E%s: (%s,%s)" % (p, a, b))
        pole = EK_for_EG_2.NahozTochek(a, b, p)
        l = int(input("1 - выбор открытого ключа\n2 - зашифровать текст\n3 - расшифровать зашифрованный(2) текст\n4 - расшифровать сообщение\n5 - выход\n"))
        if l == 1:#ввод точки - открытого ключа
            C = EK_for_EG_2.VvodTochek(pole)
        elif l == 2:#шифруем текст
            if 'C' in locals():
                txt = input("Введите сообщение, которое нужно зашифровать: ")
                masstoch = np.zeros((len(txt), 2))
                tochki = Preobrazovanie(txt, masstoch, symvoli, kodirovka)
                f = int(input("1 - найти открытый ключ получателя\n2 - ввести открытый ключ получателя\n"))
                if f == 1:
                    e = int(input("Введите закрытый ключ получателя e: "))
                    eC = OpenKeyB(e, C, p, a)
                elif f == 2:
                    eC = EK_for_EG_2.VvodTochek(pole)
                print("eC =", eC)
                k = int(input("Введите закрытый ключ отправителя k: "))
                kC = EK_for_EG_2.Umnozenie(C, k, p, a)
                for i in range(len(txt)):
                    masstoch[i] = Encryption(tochki[i], k, eC, p, a)#шифрую каждую точку
                print("kC =", kC, "\n", masstoch)
            else:
                print("Сначала введите открытый ключ.")
        elif l == 3:#расшифровать, что зашифровале в пункте 2
            if 'kC' in locals() and 'masstoch' in locals():
                e = int(input("Введите закрытый ключ получателя e: "))
                enkmass = np.zeros((len(masstoch), 2))
                for i in range(len(masstoch)):
                    enkmass[i] = Decryption(masstoch[i], kC, e, p, a, pole)
                m = [m for m in 'a'*len(enkmass)]
                soobshenie = Preobrazovanie2(enkmass, m, kodirovka, symvoli)
                print("Расшифрованное сообщение: ", ''.join(soobshenie))
            else:
                print("Сначала зашифруйте сообщение.")
        elif l == 4:#расшифровать что-то
            e = int(input("Введите закрытый ключ получателя e: "))
            print("Введите данные зашифрованного сообщения(kC и точки):")
            kC  = EK_for_EG_2.VvodTochek(pole)
            n = int(input("Введите количество точек в зашифрованном сообщении: "))
            masstoch = np.zeros((n, 2))
            for i in range(n):
                masstoch[i] = EK_for_EG_2.VvodTochek(pole)
            enkmass = np.zeros((n, 2))
            for i in range(n):
                enkmass[i] = Decryption(masstoch[i], kC, e, p, a, pole)
            m = [m for m in 'a'*n]
            soobshenie = Preobrazovanie2(enkmass, m, kodirovka, symvoli)
            print("Расшифрованное сообщение: ", ''.join(soobshenie))
        elif l == 5:#выход
            j = 1
        else:
            print("ERORR")
