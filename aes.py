from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_file(key, input_file, output_file):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as file:
        file.write(iv)
        file.write(ciphertext)

def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        iv = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Get user input
operation = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")
key = get_random_bytes(16)

# Perform encryption or decryption based on user input
if operation == 'E':
    encrypt_file(key, input_file, output_file)
    print('File encrypted successfully.')
elif operation == 'D':
    decrypt_file(key, input_file, output_file)
    print('File decrypted successfully.')
else:
    print('Invalid operation. Please choose either "E" or "D".')
