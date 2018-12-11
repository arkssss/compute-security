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

# 十六
# ans = "0214295e"
# 十
# ans = "34875742"
# bytes_mes = mes + ans
print(hashlib.sha256(bytes_mes.encode("ascii")).hexdigest())





