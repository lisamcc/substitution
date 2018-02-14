alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ `1234567890-=~!@#$%^&*()_+[]\\{}|;':\",./<>?"
key = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM <>?,./:\";'{}|[]\\+_)(*&^%$#@!~`1234567890-="

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result


def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]
    return result


unencrypted_message = "I pledge alleginace to the flag of the United States of America and to the republic for which it stands.One nation under God, indivisible, with libery and justice for all."
encrypted_message = encrypt(unencrypted_message)

print(unencrypted_message)
print(encrypted_message)
print (decrypt(encrypted_message))

