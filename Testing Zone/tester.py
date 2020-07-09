'''
Digital Fortress Tester File


Tested Messages:    Status:
Apple               Check
'''


import encryption as e
import decryption as d
import func as f

message = "apple"

print("Message:", message)
print()

print("After first encrpytion:")
en = e.firstEncrypt(message)
print(en)
print()

print("After first decrpytion:")
print(d.firstDecrypt(en))
print()

en2 = e.secondEncrypt(en)
print("After second Encryption: ")
print(en2)
print()

print("After second Decryption: ")
t = d.secondDecrypt(en2)
print(t)
print()

print("Final Message after 2nd Decryption: ")
print(d.firstDecrypt(t))
print()

print("Before Concatenation:", en2)
print()
print("Concatenated String (After Second Encryption)")

c_string = f.fourDigitConcatenation(en2)
print(c_string)

print("Deconcatenation Results:", f.fourDigitDeConcatenation(c_string))
# This is messed up.
print()
print()

print("Encrypting the Concatenated Result using Tier 3 Encryption:")
print("Encrypted Message: ")
tier3en = e.thirdEncrypt(c_string)
print(tier3en)

print("Length of Concatenated String: ", len(c_string))
print("Length of Encrypted String: ", len(tier3en))

print()
print("Obtaining tier 2 encrypted string from tier 3 via third Decryption: ")
dec2 = d.thirdDecrypt(tier3en)
print(dec2)

print("Length of dec2", len(dec2))

print("Did it work?")
if dec2 == c_string:
    print(True)
else:
    print(False)


'''
Test Cases:
20792121412111083011
dec2 = 20792121412111082011
dec2 =
021
110
Encryption:
39073112412121803011
!9sD&>6l#iuiy>5k!06$
'''

print()
tempo = f.fourDigitDeConcatenation(dec2)
print("Deconcatenated value of dec2:", tempo)
print()

tempo2 = d.secondDecrypt(tempo)
print("Second Decryption to Deconcatenated Value:", tempo2)
print()

tempo3 = d.firstDecrypt(tempo2)
print("Final Decrypted Message: ", tempo3)

print('-' * 20)
print('hello\v')
print('world')
