import pandas as pd

def read_dataset(filename):
    
        if filename=="":
            print()
            print("Файл не найден! Попробуйте еще раз!")
            filename = input()
            return read_dataset(filename)
        else:    
            full_file_path = "./" + filename
            try:
                dataset = pd.read_csv(full_file_path)
            except FileNotFoundError:
                print()
                print("Файл не найден! Попробуйте еще раз!")
                filename = input()
                return read_dataset(filename)

            pd.options.display.max_columns = 5
            pd.options.display.max_rows = 5

            print()
            print(dataset.head())

        return dataset