from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def encode_password(password: str) -> str:
    return password_hash.hash(password)

def check_password(password: str, hashed_password: str):
    return password_hash.verify(password, hashed_password)