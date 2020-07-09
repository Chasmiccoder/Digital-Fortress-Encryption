'''
Welcome to the Digital Fortress!

Date of Creation: 12th June, 2019.
Current Version: 1.0
Features:
Basic Encryption of message from its normal form to its ASCII form
'''


import func as f
import random


def firstEncrypt(message):  # Tier one encryption.
    new = ''
    delimiter = ' '

    for i in range(0, len(message)):

        new += f.charToThreeDigit(message[i]) + delimiter

    return new


def secondEncrypt(message):  # Tier two encryption.

    word_list = f.stringToList(message)  # We will receive the message as a list
    new_list = []
    # print(word_list)

    for i in range(0, len(word_list)):
        # Randomly generates an int in order to randomise the encryption type.
        r = random.randint(1, 6)

        encrypt_list = encryptList(str(word_list[i]))
        new_list.append(str(r) + f.listToString(encrypt_list[r - 1]) + ' ')

    new = f.listToString(new_list)
    return new


def encryptList(message):
    l = []
    for i in range(0, len(message)):
        l.append(message[i])

    # print("LIST", l)
    # Example: l = [0, 1, 4]

    # print("l", l)
    encrypt_list = [[l[0], l[1], l[2]],
                    [l[0], l[2], l[1]],
                    [l[1], l[0], l[2]],
                    [l[1], l[2], l[0]],
                    [l[2], l[0], l[1]],
                    [l[2], l[1], l[0]]]

    return encrypt_list


def thirdEncrypt(message):
    new = ''
    tier3List = f.randomTier3()
    for i in range(0, len(message)):

        lower = int(message[i]) * 8

        upper = lower + 7
        if upper == 80:
            upper -= 1

        new += tier3List[(random.randint(lower, upper))]
        # Basically getting a random character from the list that falls in the
        # bracket of the integer given in the message.

        # It's like saying:
        # if message[i] == '0'
        # then:      new += tier3List[random.randint(0, 10)]

    return new
