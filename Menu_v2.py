# import pandas as pd
import time
import copy

from number_types import real, positive, natural
from probability import probability, threshold
from check_filename import check_filename
from list_options import menu_list, check_user_choice, print_menu
from read_dataset import read_dataset


    
class Menu_of_classic_genetic_algorithm:

    def __init__(self, task_dict):
        try:
            self.task_dict = copy.deepcopy(task_dict)

            self.common_options = [{"n_iter": 30, "type": "natural"}, 
                                   {"eps": 0.0001, "type": "positive"},
                                   {"fitness_all_type": "average", "type": [ "average","maximum", "minimum"]},
                                   {"parent_selection_type": "roulette_wheel", "type": ["roulette_wheel",                                                          "inbriding_phenotype","inbriding_genotype","panmixy", "choose_parent_nn"]},
                                   {"cross_type": "one_point", "type": ["one_point", "discret_recombination_nn"]},
                                   {"p_cross": 0.8, "type": "probability"},
                                   {"mutation_type": "binary", "type": ["binary", "mutation_nn"]},
                                   {"p_mutation": 0.1, "type": "probability"},
                                   {"select_new_population_type":"elite","type":["elite","trunc","exclusion","selection_nn"]},
                                   {"size_of_population": 30, "type": "natural"}]
            

            self.functions_for_type = {"float": float, "int": int, "str": str,
                                       "probability": probability, "threshold": threshold,
                                       "positive": positive,"natural": natural, "real": real,
                                       "filename": check_filename,
                                       "dataset": read_dataset}

            self.unpack_common_options()

            # Дополнительные возможности для разработчика!!! Работа данного блока кода не предусмотрена!!!

            """
            self.functions_for_type.update({"dataset": self.read_dataset, "matrix": self.read_matrix})
            """

            if self.check_types_options() is "Error":
                return None

            self.task_dict_full = self.task_dict
            self.task_dict_full["options"] = self.common_options + self.task_dict_full["options"]

            time.sleep(1)

            self.input_data()
            print("SUCCESSFUL")
            self.unpack_options()
            self.unpack_task_with_options()
            
        except Exception:
            print("Что-то пошло не так ...")

    def check_types_options(self):
        for option in self.task_dict["options"]:
            if isinstance(option["type"], list):
                return None
            if option["type"] not in self.functions_for_type.keys():
                print()
                print("Ошибка типа данных! Проверьте типы!!!")
                return "Error"
        return None

    def input_data(self):
        
        dict_with_options = None
        for option in range(len(self.task_dict_full["options"])):
            option_key = list(self.task_dict_full["options"][option].keys())[0]
            type_of_data = self.task_dict_full["options"][option]["type"]
            if isinstance(type_of_data, list):
                function = check_user_choice
            else:
                function = self.functions_for_type[type_of_data]

            if type_of_data is "filename":
                message = ("Введите имя файла для '{}'\n" +
                           "(hint: файл должен находиться в текущей директории):").format(option_key)
            elif isinstance(type_of_data, list):
                dict_with_options = menu_list(type_of_data)
                message = "Выберите '{}'\n(hint: нужно ввести номер варианта):\n".format(option_key) + \
                          print_menu(dict_with_options)
            else:
                message = "Введите '{}':".format(option_key)

            print(message)

            time.sleep(0.1)

            input_data = input()
            if input_data == "" and option_key in list(self.dict_common_options.keys()):
                if isinstance(type_of_data, list):
                    input_data = self.task_dict_full["options"][option][option_key]
                else:
                    input_data = str(self.task_dict_full["options"][option][option_key])
                if isinstance(type_of_data, list):
                    self.task_dict_full["options"][option][option_key] = function(input_data, dict_with_options,
                                                                                  ret_er=False, default=True)
                else:
                    self.task_dict_full["options"][option][option_key] = function(input_data)
                print(self.task_dict_full["options"][option][option_key])
                
            elif input_data == "":
                if isinstance(type_of_data, list):
                    input_data = self.task_dict_full["options"][option][option_key]
                else:
                    input_data = str(self.task_dict_full["options"][option][option_key])
                try:
                    if isinstance(type_of_data, list):
                        self.task_dict_full["options"][option][option_key] = function(input_data, dict_with_options,
                                                                                      ret_er=True, default=True)
                    else:
                        self.task_dict_full["options"][option][option_key] = function(input_data, ret_er=True)
                    if self.task_dict_full["options"][option][option_key] != "Error":
                        print(self.task_dict_full["options"][option][option_key])
                    while self.task_dict_full["options"][option][option_key] == "Error":
                        if isinstance(type_of_data, list):
                            self.task_dict_full["options"][option][option_key] = function(input(), dict_with_options,
                                                                                          ret_er=True)
                        else:
                            self.task_dict_full["options"][option][option_key] = function(input(), ret_er=True)
                except TypeError:
                    self.task_dict_full["options"][option][option_key] = function(input_data)
            else:
                if isinstance(type_of_data, list):
                    self.task_dict_full["options"][option][option_key] = function(input_data, dict_with_options)
                else:
                    self.task_dict_full["options"][option][option_key] = function(input_data)
            print("-" * 22)

            print()
            

        return None

    def unpack_options(self):
        self.options = {}
        for option in self.task_dict["options"]:
            option_key = list(option.keys())[0]
            option_value = option[option_key]
            self.options[option_key] = option_value
        return None

    def unpack_common_options(self):
        self.dict_common_options = {} 
        for option in self.common_options:
            option_key = list(option.keys())[0]
            option_value = option[option_key]
            self.dict_common_options[option_key] = option_value
        return None

    def unpack_task_with_options(self):
        self.task_with_options = {}
        self.task_with_options["task"] = self.task_dict_full["task"]
        self.task_with_options.update(self.options)
        return None

    # Дополнительные возможности для разработчика!!! Работа данного блока кода не предусмотрена!!!

    """                            
    def read_dataset(self, filename):
    
        if filename=="":
            print()
            print("Файл не найден! Попробуйте еще раз!")
            filename = input()
            return self.read_dataset(filename)
        else:    
            full_file_path = "./" + filename
            try:
                dataset = pd.read_csv(full_file_path)
            except FileNotFoundError:
                print()
                print("Файл не найден! Попробуйте еще раз!")
                filename = input()
                return self.read_dataset(filename)

            pd.options.display.max_columns = 5
            pd.options.display.max_rows = 5

            print()
            print(dataset.head())

        return dataset


    def read_matrix(self, filename):
        full_file_path = "./" + filename

        try:
            matrix = pd.read_csv(full_file_path, header=None, sep=";").values.tolist()
        except FileNotFoundError:
            print()
            print("Файл не найден! Попробуйте еще раз!")
            filename = input()
            return self.read_matrix(filename)

        print()
        print(matrix)

        return matrix
    """
