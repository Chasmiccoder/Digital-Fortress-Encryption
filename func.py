'''
Digital Fortress Common Functions:

'''


def stringToList(message):
    # Converts a given message from string format to list format.

    word_list = []
    word = ''
    delimiter = ' '

    for i in range(0, len(message)):
        if message[i] != delimiter:
            word += message[i]

        else:
            word_list.append(word)
            word = ''

    return word_list


def listToString(message):
    # Converts a given list to string format.
    new = ''

    for i in range(0, len(message)):
        new += message[i]

    return new


def charToThreeDigit(ch):
    new_ch = str(ord(ch))

    while len(new_ch) < 3:
        new_ch = '0' + new_ch

    return new_ch


def reverseString(message):
    if len(message) == 0:
        return message
    else:
        return message[-1] + reverseString(message[:-1])


def sortList(l):
    for i in range(0, len(l) + 2):
        for j in range(0, len(l) - i - 1):
            if l[j + 1] < l[j]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def fourDigitConcatenation(message):
    new = ''
    for i in range(0, len(message)):
        if message[i] != ' ':
            new += message[i]

    return new


def fourDigitDeConcatenation(message):
    new = ''
    upper = 4
    lower = 0
    while upper <= len(message):
        new += message[lower: upper] + ' '
        lower = upper
        upper += 4

    return new


def randomTier3():
    tier3List = ['8', 's', 'e', '0', 'b', 'k', 'Z', 'c', '6', 'o', '>', 'P', '$',
                 '[', 'i', 'N', 'u', 'l', 'J', 'y', 'h', 'V', 'M', 'z', '!', 'Y',
                 '&', 'p', 'Q', 'C', '<', ']', 'G', 'L', 'K', '#', 'U', 'j', 'E',
                 '2', '*', 'W', ',', 'X', 'n', ';', '1', 'O', 'q', 'a', 'x', 'g',
                 'd', 'f', 'B', '3', ')', '7', 'D', 'T', '(', 'w', 'v', 'H', '4',
                 't', '5', ':', 'r', 'R', '.', 'm', '@', 'A', 'S', '%', 'F', '9',
                 '^', 'I']

    return tier3List


'''
To Generate a tier 3 list containing all the alphabets (Lower and Upper Case),
numbers, and a few special characters, to add on to the confusion...

import random

capital = [chr(j) for j in range(65, 91)]
small = [chr(j) for j in range(97, 123)]
numbers = [j for j in range(0, 10)]
special = ['!', '@,', '#', '$', '%', '^', '&', '*',
           '<', '>', '.', ',', ':', ';', ']', '(', ')', '[']

tier3List = capital + small + numbers + special
print("Old List: ", tier3List)
ns = []
new = []
while(len(ns) < len(tier3List)):
    r = random.randint(0, len(tier3List) - 1)

    if r not in ns:
        ns.append(r)
        new.append(tier3List[r])

print("New List: ", new)

'''
