# Digital-Fortress-Encryption-Software-
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
