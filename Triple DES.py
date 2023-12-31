import requests

# Function to print blocks of hexadecimal data
def print_blocks(hex_blocks, block_size):
    for i in range(0, len(hex_blocks), block_size):
        print(hex_blocks[i:i + block_size], ' ', end='')
    print()

# Encrypts plaintext using the provided key
def perform_encryption(secret_key, plaintext):
    # URL for encryption using Triple DES
    encrypt_url = "http://aes.cryptohack.org/triple_des/encrypt/"
    
    # Sending a request to encrypt plaintext using the provided key
    response = requests.get(encrypt_url + secret_key + '/' + plaintext + '/').json()
    
    # If there's an error in the response, raise an exception with the error message
    if response.get("error", None):
        raise ValueError(response["error"])
    
    # Return the obtained ciphertext
    return response["ciphertext"]

# Encrypts the flag using the given key
def encrypt_flag_with_key(secret_key):
    # URL for encrypting the flag using Triple DES
    encrypt_flag_url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    
    # Sending a request to encrypt the flag using the provided key
    response = requests.get(encrypt_flag_url + secret_key + '/').json()
    
    # If there's an error in the response, raise an exception with the error message
    if response.get("error", None):
        raise ValueError(response["error"])
    
    # Return the obtained ciphertext of the flag
    return response["ciphertext"]

# Defining the key and encrypting the flag
encryption_key = b'\x00'*8 + b'\xff'*8
flag_cipher_text = encrypt_flag_with_key(encryption_key.hex())

# Encryption of the flag using the key and printing the cipher in blocks
flag_block_size = 34
cipher_text = perform_encryption(encryption_key.hex(), flag_cipher_text)
print_blocks(cipher_text, 16)

# Convert ciphertext back to bytes and print
print(bytes.fromhex(cipher_text))
