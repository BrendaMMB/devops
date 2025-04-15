import base64

data_in_encode = b'cG9ydGFsX2Rldl9zZW5zaWRpYQ:X3ExciRHTlQkM0pzMGxq'
data_in_decode = b'OTM4NjgxNTU1NE11c2ljQU1hdHV0TyMkJg=='

def encode64():
    encoded_data = base64.b64encode(data_in_encode)
    print(encoded_data)

def decode64():
    decoded_data = base64.b64decode(data_in_decode)
    print(decoded_data)

# encode64()
decode64()