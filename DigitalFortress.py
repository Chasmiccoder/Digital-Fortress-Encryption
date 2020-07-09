'''
Digital Fortress Main Program:

Total Lines of Code = 426 ( which obviously includes blank lines... :P )
How to Use:
First, the program runs a check on a test message. If the ouput is not equal to
the given message, do not proceed.
Once the user is given a choice, he can enter either 1 or 2.
First mode:
Type in the message to be encrypted.

'''
import encryption as e
import decryption as d
import func as f
import time


def delayEffect():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print()


def enc(message):
    e1 = e.firstEncrypt(message)
    e2 = e.secondEncrypt(e1)
    e3 = f.fourDigitConcatenation(e2)
    e4 = e.thirdEncrypt(e3)
    return e4


def dec(message):
    d1 = d.thirdDecrypt(message)
    d2 = f.fourDigitDeConcatenation(d1)
    d3 = d.secondDecrypt(d2)
    d4 = d.firstDecrypt(d3)
    return d4


def dynamic(message):
    None


print("Testing Program...")
print()

message = input("Enter message:")
print()

print("After Encryption: ")
ENC = enc(message)
print(ENC)
print()

print("Decrypting that message:")
print(dec(ENC))
print()

while True:
    delayEffect()

    print("Today's Menu: ")
    print('''    1 - To Encrypt a message
    2 - To Decrypt a message
    3 - To Encrypt a file
    4 - To Decrypt a file
    0 - To Terminate the program''')
    print()
    choice = int(input("Enter choice: "))
    print()

    if choice == 0:
        print("Program Terminated...")
        print()
        break

    elif choice == 1:
        print("Encryption Mode: ")
        message = input("Enter message to be encrypted: ")
        print()
        print("Encrypted Value: ")
        print("Encrypted Message:", enc(message))
        print()

    elif choice == 2:
        print("Decryption Mode: ")
        message = input("Enter message to be decrypted: ")
        print("Decrypted Message:", dec(message))
        print()

    elif choice == 3:
        print("File Encryption Mode:")
        filepath = input("Enter path of the file: ")

        file = open(filepath, 'r')
        message = file.read()
        file.close()

        file = open(filepath, 'w')

        # Failsafe to prevent over encrypting something.
        if message[:3] != 'ENC':
            file.write('ENC' + enc(message))
            print("File Encrypted")
        else:
            print("This file has already been encrpyted.")
            print("No alterations done.")

        file.close()

        print()

    elif choice == 4:
        print("File Decryption Mode:")
        filepath = input("Enter path of the file: ")

        file = open(filepath, 'r')
        message = file.read()
        file.close()

        if message[:3] == 'ENC':
            file = open(filepath, 'w')
            file.write(dec(message[3:]))
            print("File Decrypted")
            file.close()
        else:
            print("This file has not been encrypted.")
            print("No alterations done")

        print()
