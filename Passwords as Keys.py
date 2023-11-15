from Crypto.Cipher import AES
import hashlib

def decrypt(ciphertext, keyword):
    cipher_text = bytes.fromhex(ciphertext)
    key = hashlib.md5(keyword.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    
    try:
        decrypted = cipher.decrypt(cipher_text)
        return decrypted
    except ValueError as e:
        return None

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

with open("/usr/share/dict/words") as f:
    for word in f.readlines():
        keyword = word.strip()
        decrypted_text = decrypt(ciphertext, keyword)
        if decrypted_text:
            try:
                decrypted_text = decrypted_text.decode('utf-8')
                print(decrypted_text)
            except UnicodeDecodeError:
                pass
