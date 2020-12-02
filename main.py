import time
text = input("Text: ")
print ("@a for all\n @s for you\n @e for all entity\n @r for random player")
selector = input("Selector: ")
print('/tellraw ' + selector + ' {"rawtext":[{"text":"' + text + '"}]}')
while True:
    time.sleep(1)
