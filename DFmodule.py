'''
Digital Fortress Module:
A module that can be imported to another file/project.
Its main purpose is to encrypt a message or decrypt an encrypted message.
'''


import encryption as e
import decryption as d
import func as f


def encrypt(message):
    e1 = e.firstEncrypt(message)
    e2 = e.secondEncrypt(e1)
    e3 = f.fourDigitConcatenation(e2)
    e4 = e.thirdEncrypt(e3)
    return e4


def decrypt(message):
    d1 = d.thirdDecrypt(message)
    d2 = f.fourDigitDeConcatenation(d1)
    d3 = d.secondDecrypt(d2)
    d4 = d.firstDecrypt(d3)
    return d4
