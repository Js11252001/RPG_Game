def Celcius2Fahrenheit(celcius):
    return (celcius * 1.8) + 32


if __name__ == "__main__":
    isrunning = True
    while isrunning:
        str = input("Convert celcius to fahrenheit(input q to quit)")
        if str.lower() == "q":
            isrunning = False
        else:
            cel = float(str)
            print("fahrenheit:", Celcius2Fahrenheit(cel))
