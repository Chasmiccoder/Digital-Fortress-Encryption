# Digital Fortress (Encryption-Software)
Inspired by Dan Brown's sci-fi book Digital Fortress, we are developing our own version of algorithm based encryption.

The way it works is that once a string is input, we first convert it to 
its ascii representation, after which the digits are shuffled according to 
a randomly selected integer from 1 to 6. That integer gets added to the encrypted string. 
Once the first layer gets encrypted, a random seed is chosen 
(according to which a list gets randomly shuffled) 
and the final output is provided (with that seed).

In order to decrypt a particular string, you need to provide the string and the seed, which acts as a 
private key. This new approach is excellent, especially due to the advent of quantum computers, because
of which standard encryption algorithms might not last. 
The only drawback is the bandwidth of the final string, which is four times as long 
as the original.

The interesting part about this type of encryption is that, if the encryption algorithm is not
known, and if the seed (private key) is known, the cryptanalysts still will not be able to decrypt
the string. This is because the string itself has been randomised in such a way that even if the same 
string gets encrypted twice (with the same seed) the odds of the string being the same (in the final output)
are one in (48)^n, where n is the number of characters in the string.
