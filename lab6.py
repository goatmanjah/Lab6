def menuDisplay():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    encodedPassword = 0
    for number in password:
        digitShifter = (int(number) + 3) % 10
        encodedPassword = encodedPassword * 10 + digitShifter
    return encodedPassword

if __name__ == '__main__':
    userInput = 0
    while True:
        menuDisplay()
        userInput = input("Please enter an option:")
        if userInput == "1":
            password = input("Please enter your password to encode:")
            encodedPassword = encode(password)
            print("Your password has been encoded and stored!")
        if userInput == "2":
            pass
        if userInput == "3":
            exit()
