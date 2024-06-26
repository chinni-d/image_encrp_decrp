from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import io

def aes_encrypt_image(image_path, key):
    # Open the image file
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    # Encrypt the image data
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    return iv + encrypted_data

def aes_decrypt_image(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    encrypted_data = encrypted_data[AES.block_size:]

    # Create a new AES cipher object with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the image data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data

# Example usage
key = get_random_bytes(16)  # AES-128
image_path = 'img.jpg'
encrypted_image = aes_encrypt_image(image_path, key)

# Save encrypted image to a file
with open('encrypted_image.aes', 'wb') as file:
    file.write(encrypted_image)

# Decrypt the image
decrypted_image = aes_decrypt_image(encrypted_image, key)

# Save decrypted image to a file
with open('decrypted_image.jpg', 'wb') as file:
    file.write(decrypted_image)