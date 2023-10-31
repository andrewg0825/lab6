# Andrew Grachoff
def encode(password):
    encodedPass = []
    for c in password:
        if int(c) < 7:
            encodedPass.append(str(int(c) + 3))
        else:
            encodedPass.append(str(int(c) - 7))

    return "".join(encodedPass)


#decode method, subtracts 3 from password- Brianna Chua
def decode(password):
    new_password = ''
    for i in password:
        new_password = new_password + str(int(i) - 3)
    return new_password


def main():
    while True:
        print("Menu \n-------------")
        print("1. Encode \n2. Decode \n3. Quit\n")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            encodedPass = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print(encodedPass)

        else:
            quit()


if __name__ == "__main__":
    main()