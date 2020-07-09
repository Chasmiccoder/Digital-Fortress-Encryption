'''
Digital Fortress Decoder:

'''


import func as f


def firstDecrypt(message):

    word_list = f.stringToList(message)
    new = ''
    # print("WordList: ", word_list)

    for i in range(0, len(word_list)):
        new += chr(int(word_list[i]))

    return new


def secondDecrypt(message):

    word_list = f.stringToList(message)
    new_list = []

    for i in range(0, len(word_list)):
        new_list.append(f.listToString(decryptList(word_list[i])) + ' ')

    new = f.listToString(new_list)
    return new


def decryptList(message):
    r = int(message[0]) - 1
    message = message[1:]
    l = message
    # print("MEESSAGE: ", message)
    decrypt_list = [[l[0], l[1], l[2]],  # Check
                    [l[0], l[2], l[1]],  # Check
                    [l[1], l[0], l[2]],  # Check
                    [l[2], l[0], l[1]],  # Check
                    [l[1], l[2], l[0]],
                    [l[2], l[1], l[0]]]  # Check
    # print("Decrypted Value: ")
    return decrypt_list[r]


def thirdDecrypt(message):
    tier3List = f.randomTier3()
    new = ''
    for i in range(0, len(message)):

        # To obtain the position at which the encrpyted character is present in the tier 3 list
        for j in range(0, len(tier3List)):
            if message[i] == tier3List[j]:
                pos = j
                break

        # e.g. if pos == 10, it will fall in the 2nd bracket (index(1) and return 1.
        # print("POS:", pos)
        pos += 1
        bracket = 0
        while pos > 8:
            pos -= 8
            bracket += 1

        new += str(bracket)

    return new
