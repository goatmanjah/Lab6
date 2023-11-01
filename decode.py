#Benjamin Stickle
#decodes the previous password

def decode(password):
    decoded_password = ""

    for n in password:
        if n < 3:
            n = 10 - (3%n)
            decoded_password += n
        else:
            n -= 3
            decoded_password += n

    return decoded_password