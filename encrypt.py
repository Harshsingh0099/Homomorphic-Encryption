from phe import paillier

# Key generation
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt two numbers
number1 = 12345
number2 = 67890
encrypted_number1 = public_key.encrypt(number1)
encrypted_number2 = public_key.encrypt(number2)

# Perform addition on encrypted data
encrypted_sum = encrypted_number1 + encrypted_number2

# Decrypt the result
decrypted_sum = private_key.decrypt(encrypted_sum)
print(f"Decrypted Sum: {decrypted_sum}")
