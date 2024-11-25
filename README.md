# Homomorphic-Encryption
This demonstrates the use of Paillier Homomorphic Encryption for both numerical data and file encryption. The Paillier cryptosystem enables secure operations on encrypted data, such as addition, without decrypting it. This feature is particularly useful for privacy-preserving computations and secure data processing.
Features
Text Encryption Example
Encrypts two numbers.
Performs addition on the encrypted data.
Decrypts the result to verify the homomorphic computation.
File Encryption Example
Encrypts a file by treating each byte as an integer.
Decrypts the file back to its original form.
Prerequisites
Python 3.x
The phe library for Paillier encryption.
Install the phe library:
pip install phe
Homomorphic Operations:
The Paillier cryptosystem supports addition and scalar multiplication on encrypted data.
Operations like subtraction or multiplication are not directly supported.
Encryption Overhead:
Ciphertext is significantly larger than plaintext due to the nature of Paillier encryption.
Security:
The keys should be securely managed to prevent unauthorized access.

