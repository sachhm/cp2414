import rsa

# Generate key pairs (public and private keys)
(public_key, private_key) = rsa.newkeys(2048)  # You can choose the key size

def encrypt_data(data, public_key):
    encrypted_data = rsa.encrypt(data.encode('utf-8'), public_key)
    return encrypted_data.hex()

def decrypt_data(encrypted_data, private_key):
    decrypted_data = rsa.decrypt(bytes.fromhex(encrypted_data), private_key)
    return decrypted_data.decode('utf-8')

# Example usage:
data_to_encrypt = "secret_data"

# Encrypt the data using the public key
encrypted_result = encrypt_data(data_to_encrypt, public_key)
print(f"Data to Encrypt: {data_to_encrypt}")
print(f"Encrypted Result: {encrypted_result}")

# Decrypt the data using the private key
decrypted_result = decrypt_data(encrypted_result, private_key)
print(f"Decrypted Result: {decrypted_result}")
