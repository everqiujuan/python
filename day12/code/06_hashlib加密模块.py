

# hashlib
#   加密算法：
#       md5: 不可逆的
#       AES,DES: 可逆的，
#       RSA: 非对称加密，需要公钥和私钥
#
# 明文：hello
# 密文：5d41402abc4b2a76b9719d911017c592
# md5： 明文和密文是一对一的 ， 密文是32位十六进制
#
import hashlib

m = hashlib.md5()
m.update("hello".encode())
res = m.hexdigest()
print(res)  # 5d41402abc4b2a76b9719d911017c592


