from pickle import TRUE
import ui
import func


def button_click():
    while True:
        choicee = input("что делаем 1 - добавление, 2 - поиск, 3 - выход, 4 - удалить ")
        
        file = func.read_file()

        if choicee == '1':
            alldata = ui.input_all_data()
            func.writing_file(alldata)
            # file = func.read_file()

        elif choicee == '2':
            
            what_find = input("Введите данные для поиска: ")
            func.find_surname(what_find,file)        
        elif choicee == '3': break
        elif choicee == '4': 
            
            what_find = input("Введите данные для удаления: ")

            file = func.del_elem(what_find,file)            
            func.writing_file_after_del(file)

        
        else: print("Ошибка ввода!!")
