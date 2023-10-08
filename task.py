salary = 6900
cucumber = 90
strawberry = 385
veg_sale = 0.7 
tomato = 150
cookie = 140 + 140
# умножение на veg_sale - это овощи со скидкой
buy = (cucumber * 5 + tomato * 4 ) * veg_sale + cookie #покупка
print(salary - buy)

print(f"у таксиста Вани из {salary} рублей после траты {buy} рублей осталось {salary - buy} рублей")


print(10//3) #целочисленное деление 
print(10%3) #деление с остатком

left = salary - buy
travel= 36
stock = 134.65
money = 5886
print(f"таксист Ваня сможет купить {left//stock} акций")

print(f"У таксиста Вани останется {int(left % stock)} рублей, проезд стоит {travel} рублей")

number = int(input("Введите число: "))
first = number // 100
second = number //10 % 10
third = number % 10
print(third + first + second)

ДЗ
a = 647
b = 170
c = 30
d = (a // c)
print(f"Кол-во по вертикали {d}")
f = (b // c)
print(f"Кол-во по горизонтали {f}")
q = (d * f)
print(f"Общее кол-во квадратов {q}")
