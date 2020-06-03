import jwt

def create_token(data, secret):
    return jwt.encode(data, secret , algorithm ='HS256')

def verify_signature(token):
    secret = "acelera"
    try:
        return jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.InvalidTokenError:
        return {"error": 2}