
import hashlib

s_salt="kabijobada"


def u_and_p_hash(user_name,password):
    u_and_p=user_name+password+s_salt

    result = hashlib.md5(u_and_p.encode('utf-8'))
    return result.hexdigest()
def p_hash(password):

    p=password+s_salt
    result = hashlib.md5(p.encode('utf-8'))
    return result.hexdigest()


uname= "ras" 
password = "sadas"

after_hash= u_and_p_hash(uname,password)

print(after_hash)

