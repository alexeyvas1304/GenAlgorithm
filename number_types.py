def real(number, ret_er=False):
    number_lst = list(map(str, list(range(10)))) + [".", "+", "-", "e"]
    for i in number:
        if i not in number_lst:
            print()
            print("Error: {} - не число!".format(number))
            print("Повторите ввод")
            if ret_er:
                return "Error"
            return real(input())
    try:
        return float(number)
    except ValueError:
        print()
        print("Error: {} - не число!".format(number))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return real(input())


def positive(number, ret_er=False):
    number = real(number, ret_er)
    if number == "Error" and ret_er:
        return "Error"
    if number > 0:
        return number
    else:
        print()
        print("Error: {} <= 0".format(number))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return positive(input())


def whole(number, ret_er=False):
    number = real(number, ret_er)
    if number == "Error" and ret_er:
        return "Error"
    if number - int(number) == 0:
        return int(number)
    else:
        print()
        print("Error: {} - нецелое число".format(number))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return whole(input())


def natural(number, ret_er=False):
    number = real(number, ret_er)
    if number == "Error" and ret_er:
        return "Error"
    if number > 0 and number - int(number) == 0:
        return int(number)
    else:
        print()
        print("Error: {} - ненатуральное число".format(number))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return natural(input())
