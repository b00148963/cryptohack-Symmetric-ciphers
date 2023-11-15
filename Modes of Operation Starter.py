import requests

# URL to the encryption and decryption endpoint
url = 'http://aes.cryptohack.org/block_cipher_starter'

# Fetch the ciphertext from server
encrypt_request = requests.get(f"{url}/encrypt_flag")
encrypted_data = encrypt_request.json()
ciphertext = encrypted_data["ciphertext"]

# Request decryption of obtained ciphertext
decrypt_request = requests.get(f"{url}/decrypt/{ciphertext}")
decrypted_data = decrypt_request.json()
plaintext_hex = decrypted_data["plaintext"]

# Convert hexadecimal plaintext to bytes
plaintext_bytes = bytes.fromhex(plaintext_hex)
print(plaintext_bytes)
