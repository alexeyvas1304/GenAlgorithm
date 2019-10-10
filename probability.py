from number_types import real


def probability(number, ret_er=False):
    number = real(number, ret_er)
    if number == "Error" and ret_er:
        return "Error"
    if 0 <= number <= 1:
        return number
    else:
        print()
        if number < 0:
            print("Error: {} < 0".format(number))
        else:
            print("Error: {} > 1".format(number))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return probability(input())
