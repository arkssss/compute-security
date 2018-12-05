# from ecdsa import SigningKey, VerifyingKey, NIST384p, util, NIST224p

# vk2 可以通过 vk 构造
# sk = SigningKey.generate(curve=NIST224p)
# vk = sk.get_verifying_key()
# signature = sk.sign("message".encode("utf-8"))
# vk_string = vk.to_string()
# vk2 = VerifyingKey.from_string(vk_string, curve=NIST384p)
# print(vk2.verify(signature, "message".encode("utf-8")))
#
#
# vk = VerifyingKey.from_pem(open("vk.pem").read())


# from ecdsa import SigningKey
# sk = SigningKey(True)
# sk.from_secret_exponent()
# vk = sk.get_verifying_key()
# open("private.pem", "w").write(str(sk.to_pem()))
# open("public.pem", "w").write(str(vk.to_pem()))
#
# sk = SigningKey.from_pem(open("private.pem").read())
# message = open("message", "rb").read()
# sig = sk.sign(message)
# open("signature", "wb").write(sig)

import ecdsa
import hashlib
from ecdsa import VerifyingKey, ellipticcurve, util, curves, SigningKey
#


sk = SigningKey.generate(curve=curves.NIST224p, hashfunc=hashlib.sha256)  # uses NIST192p
vk = sk.get_verifying_key()
signature = sk.sign(bytearray.fromhex("abcd"))


puk_x = vk.pubkey.point.x()
puk_y = vk.pubkey.point.y()


_r = 26959946667150639794667015087019625940457807714424391721682722368061   # order


# 构造公钥的pk(在给定的点的情况下)
public_point = ellipticcurve.Point(curves.NIST224p.curve, puk_x, puk_y, _r)
vk = VerifyingKey.from_public_point(public_point, curve=curves.NIST224p, hashfunc=hashlib.sha256)

print(vk.verify(signature, bytearray.fromhex("abcd"), hashfunc=hashlib.sha256))

hex_string = "1abc"
data = bytearray.fromhex(hex_string)
print(type(data))
print(data)



# signature = sk.sign("message".encode("ascii"), hashfunc=hashlib.sha256)
# # print(chardet.detect(signature))
# # print(len(signature.hex()))
# # print(len(signature))
# # print(signature)
# # # print(vk.verify(signature, "message".encode("utf-8")))
#
#
# # # 这里不能直接用NIST224p, 因为ellipticcurve.Point ， 传入的为curveFp 类型的， 而非curve
# _p = 26959946667150639794667015087019630673557916260026308143510066298881
# _b = 0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
# curve_224 = ellipticcurve.CurveFp(_p, -3, _b)
#
# # 构造公钥的pk(在给定的点的情况下)
# public_point = ellipticcurve.Point(curve_224, 0xA374F7774070CD8BECCDD5B01450FFBC0033EE5FFBFEC7829C10DDD1,
#                                    0xF484F9AF3B9DD12C93F5DA7971333C3A0DCDBD20865CCE59145D9180)
# vk = VerifyingKey.from_public_point(public_point, curve=NIST224p, hashfunc=hashlib.sha256)

# s = "bcba784f921c5e881a4788cde432641921d1051375fe0a241c06f54f"
# s_int = int(s, 16)
# r = "992b9420a31dab111e51f8d3bc508c8db84db65dd1d208a7a458947e"
# r_int = int(r, 16)
# the_order = vk.pubkey.order
# assert vk.verify(signature, "message".encode("ascii"), hashfunc=hashlib.sha256)



import binascii

# print("5d2c".encode("ascii"))


# -----------------------------  work space
# 这里不能直接用NIST224p, 因为ellipticcurve.Point ， 传入的为curveFp 类型的， 而非curve
# _p = 26959946667150639794667015087019630673557916260026308143510066298881
# _b = 0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
_r = 26959946667150639794667015087019625940457807714424391721682722368061   # order
x = "0xA374F7774070CD8BECCDD5B01450FFBC0033EE5FFBFEC7829C10DDD1"
x_int = int(x, 16)
y = "0xF484F9AF3B9DD12C93F5DA7971333C3A0DCDBD20865CCE59145D9180"
y_int = int(y, 16)

# curve_224 = ellipticcurve.CurveFp(_p, -3, _b)

# 构造公钥的pk(在给定的点的情况下)
public_point = ellipticcurve.Point(curves.NIST224p.curve, x_int, y_int, _r)
vk = VerifyingKey.from_public_point(public_point, curve=curves.NIST224p, hashfunc=hashlib.sha256)

r = "992b9420a31dab111e51f8d3bc508c8db84db65dd1d208a7a458947e"
r_int = int(r, 16)
s = "bcba784f921c5e881a4788cde432641921d1051375fe0a241c06f54f"
s_int = int(s, 16)

the_order = vk.pubkey.order
# 构造签名
sig = util.sigencode_string(r_int, s_int, the_order)

vk.verify(sig, "8288ce64041c6b42d09ca89eb0cb7e0f62c62374cb8048934fb4d794711819d3869ef2a75cf16601c1cb639f36b27c6274662bf22e78ef8185c5699dd4ed31c7cabed8d82eae3062b42217504908ffb19cdabb399d492010b50208ac4452fb0be6e6ea797b083acbad408fb84a2c5106cb99c1ed6ed88218d208c19eadabff9635a67d3ee777673db8eb62b9b68b5114c2f8269b3eb4ff72489c48f0dfd2e2bb74108018f4454b8404bef0b38e6368eb6bd483add775567d7eb1eed73790cf107ad82696365c8a2fb4d999291024f0cc086754afdd77562af93b11b0ae7a1b8346bfa320e61a7ddbd198aae981fd7eec08d3f1d3c0de9494f1319a186b30dfe2".encode("ascii"), hashfunc=hashlib.sha256)
#
# # a = 0
# try:
#     a = (1/2)
# except ImportError:
#     exit()
# print(a)


# ----------------------end

# vk = VerifyingKey.from_pem(open("public.pem").read())
# message = open("message","rb").read()
# sig = open("signature","rb").read()
# try:
#     vk.verify(sig, message)
#     print ("good signature")
#     except BadSignatureError:
#     print ()"BAD SIGNATURE"

# print(sha3_224("123".encode("utf-8")))
# print(sha256("123".encode("utf-8")))


# string = "123123"
#
# sha256 = hashlib.sha1()
# sha256.update(string.encode('utf-8'))
# res = sha256.hexdigest()
# print(len(res))
# print("sha256 加密结果:", res)
#
#
# sha224 = hashlib.sha224()
# sha224.update(string.encode('utf-8'))
# res = sha224.hexdigest()
# print(len(res))
# print("sha3_224加密结果:", res)





