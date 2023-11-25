
import random

def robot_clean():
    print("Робот, убиается")
    
def robot_up_walk():
    print("Рбот идет вперед")
    
def robot_left_walk():
    print("Рбот идет вправо")
    
def robot_right_walk():
    print("Рбот идет влево")
    
def robot_down_walk():
    print("Робот идет назад")
    
for i in range(1):
    robot_clean()
    
def robot_scan():
    items = ["Дерево", "Стекло", "Cтекло"]
    one_item = random.choice(items)
    print(f"Робот нашел предмет {one_item}")
    return one_item

backpack = []
def robot_take(item):
    global backpack
    backpack.append(item)
    print(backpack)

    
while True:
    key = input("Введите клавишу: ")
    if key == "w":
        robot_up_walk()
    elif key == "s":
        robot_down_walk()
    elif key == "a":
        robot_left_walk()
    elif key == "d":
        robot_right_walk()
    elif key == "q":
        predmet = robot_scan()
        robot_take(predmet)
        
    