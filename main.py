import time
print("Можно использовать цветовые коды!")
print("§1 Синий\n§2 Голубой\n§3 Зеленый\n§4 Красный\n§5 Розовый\n§6 Золотой")
text = input("Текст: ")
print ("@a Для всех\n @s Для вас\n @e Для всех сущностей\n @r Для случайного игрока")
selector = input("Селектор: ")
print('/tellraw ' + selector + ' {"rawtext":[{"text":"' + text + '"}]}')
while True:
    time.sleep(1)
