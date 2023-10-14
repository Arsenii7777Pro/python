exp = 2 + 2 == 4
print(exp)
print(type(exp)) # логический (true) / (folse)
if exp:
    print("Вы видите эту строку")
    
age = 13
if age ==13:
    print("Тебе 13 лет")
if age > 13:
    print("тебе больше 13 лет")
if age >= 27:
    print("Тебе больше 27 или тебе 27 лет")
if age < 30:
    print("Ты младше 30")
    if age <= 30:
        print("Ты младше 30 или тебе 30")
if age != 30:
    print("Тебе не 30 лет")
    
    
    #number = int(input("введите число: "))
    if number % 2 == 1:
        print("Число нечетное")
    else:
        print("Число четное")
    
    
temp = int(input("Введите температуру воздуха: "))
if temp < 0:
    print("Холодно")
elif temp < 15:
    print("Прохладно")
elif temp < 20:
    print("Тепло")
elif temp < 30:
    print("Жарко")
else:
    print("ООчень жарко")