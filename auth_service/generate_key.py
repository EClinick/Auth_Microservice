import secrets
import base64

# Generate a secure 256-bit key
key = secrets.token_bytes(32)
# Convert to base64 for storage
secret_key = base64.b64encode(key).decode('utf-8')
print(secret_key)