salary = 6900
veg_sale = 0.7
cucumber = 90
tomato = 150
strawberry = 385 
cookies = 140 + 140

by = (cucumber * 5 + tomato * 4) * veg_sale + cookies # сумма покупки
print(f"У таксиста из {salary} рублей после траты {by} рублей осталось {salary - by} рублей")
print(10 // 3) # целочисленное деление
print(10 % 3) # остаток

left = salary - by
stock = 134.65
travel = 36

print(f"Таксист Ваня сможет купить {left // stock} акций")
print(f"У таксиста Вани остается {int(left % stock)} рублей, проезд стоит {travel} рублей")

a = int(input("Введите длину квадрата: "))
s = a * a
p = a * 4
print(f"Площадь квадрата со стороной {a} равна {s}")
