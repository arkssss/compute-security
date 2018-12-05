"""
最后的挖矿程序
"""
import hashlib

mes = "Congratulations! You have successfully solved the puzzle! Good job!"

# 寻找答案
i = 0x01
while 1:
    str_hex = hex(i)[2:]
    len_str = len(str_hex)
    if len_str % 2 is 1:
        str_hex = "0" + str_hex
    bytes_mes = mes+str_hex
    if hashlib.sha256(bytes_mes.encode('ascii')).hexdigest()[:6] == "000000":
        print(str_hex)
        break
    i += 1

# r = "abcd1234
# print(int(r, 16))
# print(bytes_mes.hex())

# r = b'\x10\x40\x86\x97\x51'
# m = b'123'
# r = b'\x0f\x5c\x34'
# print(int(r, 16))s


# print(bytes.fromhex(str(r)))

# print(bytes_mes + r)
#
# print(hashlib.sha256(bytes_mes + r).hexdigest())

# r = "0f5c34"
# # print(int(r, 16))
# print(hashlib.sha256(bytes_mes + bytes.fromhex(r)).hexdigest())


# test = "42091992"
# print(int(test, 16))
#
# test2 = "Congratulations! You have successfully solved the puzzle! Good job!1040869751"
# print(hashlib.sha256(test2.encode("ascii")).hexdigest())

# 十六
ans = "0214295e"
# 十
ans = "34875742"
ord = int(ans, 16)
print(ord)


