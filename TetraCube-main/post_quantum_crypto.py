
import hashlib
import base64
import secrets

def pq_hash(input_str: str, salt: str = "") -> str:
    """
    Post-Quantum Safe Hashing Simulation using SHA-512 + Base64 entropy mix.
    (Note: Replace with Kyber/Sphincs+ for production)
    """
    full_input = (input_str + salt).encode("utf-8")
    digest = hashlib.sha512(full_input).digest()
    encoded = base64.urlsafe_b64encode(digest).decode("utf-8")
    return encoded[:64]  # Truncate for credential compactness

def generate_entropy_key(length: int = 64) -> str:
    return base64.urlsafe_b64encode(secrets.token_bytes(length)).decode("utf-8")[:length]
