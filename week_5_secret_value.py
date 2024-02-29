import hashlib
import os

def secret_hash(data, secret_key):
    # Combine the data and secret_key
    combined_data = data.encode('utf-8') + secret_key.encode('utf-8')

    # Use hashlib to create a hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the combined data
    hash_object.update(combined_data)

    # Get the hexadecimal representation of the hash
    hashed_value = hash_object.hexdigest()

    return hashed_value

# Example usage:
data_to_hash = "example_data"
secret_key_length = 16  # You can choose any length for your secret key
secret_key = os.urandom(secret_key_length).hex()

hashed_result = secret_hash(data_to_hash, secret_key)

print(f"Data: {data_to_hash}")
print(f"Secret Key: {secret_key}")
print(f"Hashed Result: {hashed_result}")
