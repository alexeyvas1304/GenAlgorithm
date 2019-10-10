def menu_list(lst):
    dict_of_lst = {}
    for i in range(len(lst)):
        dict_of_lst[i+1] = lst[i]
    return dict_of_lst


def print_menu(dict_of_lst):
    message = str()
    for key, value in dict_of_lst.items():
        message += "    {}. {}\n".format(str(key), str(value))
    return message


def check_user_choice(choice, dict_of_options, ret_er=False, default=False):
    if choice in map(str, dict_of_options):
        print("\n{}. {}".format(choice, dict_of_options[int(choice)]))
        return dict_of_options[int(choice)]
    else:
        if default and choice in dict_of_options.values():
            return choice
        print("'{}' - такого варианта нет!".format(choice))
        print("Повторите ввод")
        if ret_er:
            return "Error"
        return check_user_choice(input(), dict_of_options)
