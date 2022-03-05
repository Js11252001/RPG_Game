isRunning = True
while isRunning:
    str = input("quit or not?(input q to quit)")
    if str.lower() == "q":
        isRunning = False
print('Loop ended.')