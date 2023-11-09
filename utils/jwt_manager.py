from jwt import encode, decode

def create_token(data: dict) -> str:
    """Encode data as a token using JWT."""
    token: str = encode(payload=data, key='1234*', algorithm='HS256')
    return token

def validate_token(token: str) -> dict: # type: ignore
    data: dict = decode(token, key='1234*', algorithms=['HS256'])
    return data