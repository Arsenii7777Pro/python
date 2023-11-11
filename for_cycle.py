
# a = int(input("Довай пиши"))
# for counter in range(a):
#     print("Silense golden")
# for i in range(1, 10):
#     print(i)
for i in range(10, 51, 10):
    print(i)
    
for i in "cegma":
    print(i)

menu = [
    "Цезарь",
    "Пити",
    "Канапе"
]
for dish in menu:
    print(f"{dish} - это вкусно")
    
menu[3] = "Бутерброт"
for dish in menu:
    print(f"{dish} - это вкусно")
    
    