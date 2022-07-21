def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))


def out_black(text):
    print("\033[30m {}".format(text))


def r(x: float) -> float:
    """Точність округлення"""
    x = round(x, 4)
    if float(x) == int(x):
        return int(x)
    else:
        return x


def par(parametr: float) -> str:
    """Для вивіду. Негативні числа закидає в скобки и округлює функцією "r" """
    if parametr < 0:
        return "(" + str(r(parametr)) + ")"
    else:
        return str(r(parametr))


def printf(name: str, value: int or float):
    """Форматованний вивід змінної з округленням"""
    print("{} = {}".format(name, r(value)))


def func_Y(x):
    return x**3+2*x**2-1


def der_funcY(x):
    return 3*x**2+4*x


def double_der_funcY(x):
    return 6*x + 4


def half_division(a, b, E):
    """сужает диапазон до нужой точности и возвращает ответ"""
    out_red("Метод половинного деления")
    out_black("")
    print("a = {}, b = {}".format(a, b))
    c = (a + b) / 2
    print("c = (a + b) / 2 = {}".format(r(c)))
    print("|func(c)| = {}".format(r(abs(func_Y(c)))))
    print("E = {}".format(E))
    print("func(a) = {}".format(r(func_Y(a))))
    print("func(b) = {}".format(r(func_Y(b))))
    print("func(c) = {}".format(r(func_Y(c))))
    if abs(func_Y(c)) < E:
        print("\nРезультат: x = {}, точність = {}\n".format(r(c), E))
        return c
    if func_Y(a) * func_Y(c) < 0:
        print("Нові точки А і С")
        return half_division(a, c, E)
    if func_Y(b) * func_Y(c) < 0:
        print("Нові точки В і С")
        return half_division(b, c, E)


def hord_division(a, b, vupadok, E):
    """метод хорд"""
    out_blue("Метод хорд")
    out_black("")
    if vupadok == 1:
        """коли знак першої і другої похідної збігається"""
        x = a - (func_Y(a) * (b - a)) / (func_Y(b) - func_Y(a))
        print("A = {}, B = {} (нерухома)".format(r(a), r(b)))
        print("func_Y(a) = {}, func_Y(b) = {}".format(r(func_Y(a)), r(func_Y(b))))
        print("x = a - (func_Y(a) * (b -a) ) / ( func_Y(b) - func_Y(a) ) = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(a), E))
        if abs(x - a) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return hord_division(x, b, vupadok, E)
    if vupadok == 2:
        """коли у першої і другої похідної різні знаки"""
        x = b - (func_Y(b) * (b - a)) / (func_Y(b) - func_Y(a))
        print("A = {} (нерухома), B = {}".format(r(a), r(b)))
        print("func_Y(a) = {}, func_Y(b) = {}".format(r(func_Y(a)), r(func_Y(b))))
        print("x = b - (func_Y(b) * (b - a)) / (func_Y(b) - func_Y(a)) = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(a), E))
        if abs(x - b) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return hord_division(a, x, vupadok, E)


def nuton(a, b, vupadok, E):
    out_red("Метод Ньютона (дотичних)")
    out_black("")
    """метод хорд"""
    if vupadok == 1:
        """коли знак першої і другої похідної збігається"""
        x = b - func_Y(b) / der_funcY(b)
        print("A = {} (нерухома) , B = {}".format(r(a), r(b)))
        print("func_Y(b) = {}".format(r(func_Y(b))))
        print("y' (b) = {}".format(r(der_funcY(b))))
        print("b - func_Y(b) / pox_funcY(b) = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(b), E))
        if abs(x - b) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return nuton(a, x, vupadok, E)
    if vupadok == 2:
        """коли у першої і другої похідної різні знаки"""
        x = a - func_Y(a) / der_funcY(a)
        print("A = {} , B = {} (нерухома)".format(r(a), r(b)))
        print("func_Y(a) = {}".format(r(func_Y(a))))
        print("y' (a) = {}".format(r(der_funcY(a))))
        print("x = a - func_Y(a) / pox_funcY(a) = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(a), E))
        if abs(x - a) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return nuton(x, b, vupadok, E)


def dif_nuton(a, b, vupadok, E, pox_x_x0):
    out_blue("Измененний метод дотичних (в знаменателе стабильная пох. от одной с точек)")
    out_black("")
    """метод хорд"""
    if vupadok == 1:
        """коли знак першої і другої похідної збігається"""
        x = b - func_Y(b) / pox_x_x0
        print("pox_x_x0 = {}".format(pox_x_x0))
        print("A = {} (нерухома) , B = {}".format(r(a), r(b)))
        print("func_Y(b) = {}".format(r(func_Y(b))))
        print("x = b - func_Y(b) / pox_x_x0 = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(b), E))
        if abs(x - b) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return dif_nuton(a, x, vupadok, E, pox_x_x0)
    if vupadok == 2:
        """коли у першої і другої похідної різні знаки"""
        x = a - func_Y(a) / pox_x_x0
        print("pox_x_x0 = {}".format(pox_x_x0))
        print("A = {} , B = {} (нерухома)".format(r(a), r(b)))
        print("func_Y(a) = {}".format(r(func_Y(a))))
        print("x = a - func_Y(a) / pox_x_x0 = {}".format(r(x)))
        print("|Xn+1 - Xn| < E")
        print("|{} - {}| ? {}".format(r(x), r(a), E))
        if abs(x - a) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return dif_nuton(x, b, vupadok, E, pox_x_x0)


def mult(a, b, vupadok, E):
    out_red("Хорда в перемешку с Ньютоном")
    out_black("")
    if vupadok == 1:
        x = b - func_Y(b) / der_funcY(b)
        print("A = {} (нерухома) , B = {}".format(r(a), r(b)))
        print("func_Y(b) = {}".format(r(func_Y(b))))
        print("y' (b) = {}".format(r(der_funcY(b))))
        print("x(dot) = b - func_Y(b) / pox_funcY(b) = {}".format(r(x)))

        x1 = a - (func_Y(a) * (x - a)) / (func_Y(x) - func_Y(a))
        print("A = {}, X(dot) = {} (нерухома)".format(r(a), r(x)))
        print("func_Y(a) = {}, func_Y(b) = {}".format(r(func_Y(a)), r(func_Y(b))))
        print("x = a - (func_Y(a) * (x - a)) / (func_Y(x) - func_Y(a)) = {}".format(r(x1)))
        print("|X(dot) - X(hord)| < E")
        print("|{} - {}| ? {}".format(r(x), r(x1), E))
        if abs(x - x1) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return mult(x1, x, vupadok, E)
    if vupadok == 2:
        x = a - func_Y(a) / der_funcY(a)
        print("A = {} , B = {} (нерухома)".format(r(a), r(b)))
        print("func_Y(a) = {}".format(r(func_Y(a))))
        print("y' (a) = {}".format(r(der_funcY(a))))
        print("x(dot) = a - func_Y(a) / pox_funcY(a) = {}".format(r(x)))

        x1 = b - (func_Y(b) * (b - x)) / (func_Y(b) - func_Y(x))
        print("x(dot) = {} (нерухома), B = {}".format(r(x), r(b)))
        print("func_Y(a) = {}, func_Y(b) = {}".format(r(func_Y(a)), r(func_Y(b))))
        print("x = b - (func_Y(b) * (b - x)) / (func_Y(b) - func_Y(x)) = {}".format(r(x1)))

        if abs(x - x1) < E:
            print("\nx = {}\n".format(r(x)))
            return x
        return mult(x1, x, vupadok, E)


def iter(a, b, E):
    out_blue("Ітераційний метод")
    out_black("")
    print("A = {}".format(a))
    print("B = {}".format(b))
    x0 = (a + b) / 2
    print("x0 = {}".format(r(x0)))
    if der_funcY(a) * der_funcY(b) > 0:
        print("pox_funcY(a) = {}".format(r(der_funcY(a))))
        print("pox_funcY(b) = {}".format(r(der_funcY(b))))
        R = max(abs(der_funcY(a)), abs(der_funcY(b)))
        print("r = max(|y'(a)|, |y'(b)'| = {}".format(r(R)))
        if der_funcY(a) > 0:
            lam = -(1 / R) / 2
            print("lam = - (1 / R) / 2 = {}".format(r(lam)))
        else:
            lam = (1 / R) / 2
            print("lam = (1 / R) / 2 = {}".format(r(lam)))
        def func_asimp(x, lam, E):
            y = lam*func_Y(x) + x
            print("y = {} * func_Y(x) + {}".format(r(lam), r(x)))
            print("x_набл = {}".format(y))
            if abs(y-x)<E:
                return y
            func_asimp(y, lam, E)
        func_asimp(x0, lam, E)


def fiend_interval(a, b, step, E):
    for i in range(a, b + step, step):
        """ищем участок, на котором значение в точке разные"""
        if abs(func_Y(i)) < E:
            print("\nРезультат: x = {}, точність = {}".format(r(i), E))
            return i
        if i == a:
            continue
        print(" func_Y(a) = {}".format(r(func_Y(i))))
        print(" func_Y(b) = {}\n".format(r(func_Y(i - step))))
        if func_Y(i) * func_Y(i - step) < 0:
            print("Знаки різні\n")
            a = i - step
            print("a = " + str(a))
            b = i
            print("b = " + str(b))
            half_division(a, b, E)
            iter(a, b, E)
            print("\npox_funcY(a) = {}".format(r(der_funcY(a))))
            print("pox_funcY(b) = {}".format(r(der_funcY(b))))
            print("pox_pox_funcY(a) = {}".format(r(double_der_funcY(a))))
            print("pox_pox_funcY(b) = {}".format(r(double_der_funcY(b))))
            if der_funcY(a) * der_funcY(b) > 0 and double_der_funcY(a) * double_der_funcY(b) > 0:
                if der_funcY(a) * double_der_funcY(a) > 0:
                    print("Знаки першої і другої похідної збігаються\n")
                    vupadok = 1
                else:
                    print("Знаки першої і другої похідної не збігаються\n")
                    vupadok = 2
                hord_division(a, b, vupadok, E)
                nuton(a, b, vupadok, E)
                if vupadok == 1:
                    dif_nuton(a, b, vupadok, E, der_funcY(b))
                else:
                    dif_nuton(a, b, vupadok, E, der_funcY(a))
                mult(a, b, vupadok, E)
            break


a = 0
b = 2
step = 1
E = 0.001
lis = fiend_interval(a, b, step, E)

print(lis)