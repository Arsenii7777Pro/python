import random
pl_name = input("Введите  ваше имя")
print(f"{pl_name} добро пожаловать в игру :")
print("Компьютер загадал число от 1 до 100.попоробуй отгодать")
comp_number = random.randint(1, 100) 
tries = 11
while tries <= 10:
      tries -= 1   
      print(f"{pl_name} попытка №{tries}")
      my_number = int(input(f"{pl_name}Введите число"))

         
      if my_number > comp_number:
        print(f"{pl_name} загаданое число меньше ")
      elif my_number < comp_number:
        print("Загаданое число больше")
      elif my_number == comp_number:
        print(f"{pl_name} вот ваш миллион доларов $$$$")
        break
      if tries == 0:
        print(f"Правильный ответ - {comp_number}. {pl_name} проииграл все имущесттво")
        break
       
