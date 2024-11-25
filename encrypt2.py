import os
from phe import paillier

# Function to encrypt a file
def encrypt_file(input_file, output_file, public_key):
    with open(input_file, "rb") as f_in, open(output_file, "w") as f_out:
        while (byte := f_in.read(1)):
            # Convert byte to integer
            byte_int = int.from_bytes(byte, "big")
            # Encrypt the byte
            encrypted_byte = public_key.encrypt(byte_int)
            # Write the encrypted byte to the file
            f_out.write(str(encrypted_byte.ciphertext()) + "\n")

# Function to decrypt a file
def decrypt_file(encrypted_file, output_file, private_key):
    with open(encrypted_file, "r") as f_in, open(output_file, "wb") as f_out:
        for line in f_in:
            # Convert the ciphertext back to an integer
            encrypted_byte = paillier.EncryptedNumber(public_key, int(line.strip()))
            # Decrypt the byte
            decrypted_byte = private_key.decrypt(encrypted_byte)
            # Write the decrypted byte to the output file
            f_out.write(decrypted_byte.to_bytes(1, "big"))

# Generate key pair
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt the file
encrypt_file("plaintext_file.txt", "encrypted_file.txt", public_key)

# Decrypt the file
decrypt_file("encrypted_file.txt", "decrypted_file.txt", private_key)
