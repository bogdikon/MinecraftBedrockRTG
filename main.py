import time
print("You can use § codes!")
print("§1 Blue\n§2 Light Blue\n§3 Green\n§4 Red\n§5 Pink\n§6 Gold")
text = input("Text: ")
print ("@a for all\n @s for you\n @e for all entity\n @r for random player")
selector = input("Selector: ")
print('/tellraw ' + selector + ' {"rawtext":[{"text":"' + text + '"}]}')
while True:
    time.sleep(1)