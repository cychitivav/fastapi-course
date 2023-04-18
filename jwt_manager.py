from jwt import encode, decode


def generate_token(data: dict):
    token: str = encode(payload=data, key='secret', algorithm='HS256') 

    return token


def verify_token(token: str):
    decoded_token = decode(token, 'secret', algorithms=['HS256'])

    return decoded_token
