import random
print("Добро пожаловать в игру")
print("Компьютер загадал число от 1 до 1000.попоробуй отгодать")
comp_number = random.randint(1, 1000) 
attempts = 10
while attempts != 0:
    print(f"У вас отсатлось {attempts} попыток")
    attempts -= 1
    my_number = input("ведите число: ")
    if not my_number.isdigit():
        continue
        print("Число вводи гений")
    my_number = int(my_number)
    attempts -= 1
    
    if my_number > comp_number:
        print("Загаданое число меньше")
    elif my_number < comp_number:
        print("Загаданое число больше")
    elif my_number == comp_number:
        print("Угадал.Вот ваш миллион доларов$$$$$")
        break
    if attempts == 0:
        print(f"Правильный ответ - {comp_number}")
        break