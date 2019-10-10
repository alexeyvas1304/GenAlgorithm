import os.path


def check_filename(filename, ret_er=False):
    full_file_path = "./" + filename
    if filename == "Error":
        print("Файл не может называться 'Error'! Попробуйте еще раз!")
        if ret_er:
            return "Error"
        return check_filename(input())
    if os.path.isfile(full_file_path):
        return filename
    else:
        print()
        print("Файл '{}' не найден! Попробуйте еще раз!".format(filename))
        if ret_er:
            return "Error"
        return check_filename(input())
