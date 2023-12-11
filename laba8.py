

def oshibka():
    print('*' * 5 + "Введено неправитльное значение!" + '*' * 5)

def PowerA3():
        try:
            a = float(input("Введите значение, которое мы сейчас возведём в степень 3:.."))
            b = a**3
            return b
        except: oshibka()


def Calc():
    Op = ''
    try:
        a = float(input("Введите значение а"))
        b = float(input("Введите значение b"))
        Op = int(input("Какое действие выполнить?\n1 - вычитание\n2 - умножение\n3 - деление\nвсё остальное - сложение"))
        if Op == 1:
            return a - b
        elif Op == 2:
            return a * b
        elif Op == 3:
            return a / b
        elif Op not in [1,2,3]:
            return a + b
    except:
        oshibka()

def Head3():
    try:
        N = int(input("Введите целое неотрицательное число:.."))
        if N == '':
            oshibka()
        N = int('3' + str(N))
        return N
    except:
        oshibka()



CallProg = input("Введите номер задачи, который Вы хотите выполнить:..")

while True:
    if CallProg == "1":
        s = input("(Если не хотите вводить 5 раз, введите 0)\n...")
        if s == 0:
            print(PowerA3())
            exit()
        elif s != 0:
            for i in range(5):
                print(PowerA3())
            exit()
        break
    elif CallProg == "2":
        print(Calc())
        break
    elif CallProg == "3":
        print(Head3())
        break
    else:
        print("Задачи под данным номером нет!")
        CallProg = input(f"\nВведите номер задачи, который Вы хотите выполнить:..")