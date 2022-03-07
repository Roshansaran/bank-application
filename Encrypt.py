import hashlib
#----------hashtabke-----------#
def Hash(binary):
    hashed = hashlib.sha384(binary)
    return hashed.hexdigest()
