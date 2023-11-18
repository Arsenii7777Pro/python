print("Это приложение Список дел")
user_name = input("Введите ваше имя: ")
todolist = []

while True:
    print("Меню:")
    print("1 - просмотреть список дел")
    print("2 - закрыть приложение")
    print("3 - добавить дело")
    user_choise = input(f"Выберите действие, {user_name}")
    if user_choise == "1":
        if len(todolist) == 0:
            print(f"Нет дел, отдыхайте, {user_name}")
        else:
            for number, do in enumerate(todolist, start=1):
                print(f"{number}. {do}")
    elif user_choise == "2":
        print(f"{user_name}, спасибо биг за использование программы")
        break
    elif user_choise =="3":
        work = input("Введите задачу или дело: ")
        if work not in todolist:
            todolist.append(work)
    else:
        print("Такого пункта нет")
    input("Нажмите инетр что бы продолжить")
    