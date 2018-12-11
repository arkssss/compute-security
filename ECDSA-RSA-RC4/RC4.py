from functools import partial


class Converter:
    @staticmethod
    def to_ascii(h):
        list_s = []
        for i in range(0,len(h),2):
            list_s.append(chr(int(h[i:i+2].upper(),16)))
        return ''.join(list_s)
    @staticmethod
    def to_hex(s):
        list_h = []
        for c in s:
            list_h.append(str(hex(ord(c)))[-2:]) #取hex转换16进制的后两位
        return ''.join(list_h)


if __name__ == "__main__":
    i = 0
    f = open('record/RC4Ciphertext.bin', 'rb')
    f2 = open('f.txt', 'w')
    # print(f.read())
    records = iter(partial(f.read, 2), b'')  # 每次2字节
    for r in records:
        j = 0
        # r_int = int.from_bytes(r, byteorder='big')  # 将 byte转化为 int
        i += 1
        # print('i={0}:{1}'.format(i, r))
        f2.write(str(r) + ' ')
        if 8 == i:
            f2.write('\n')
            i = 0
            break
    f.close()
    f2.close()



    # 二进制文件
    the_msg = b'\xd9\xa8\xa2\xfd\x12\xfcj\x82\xde\xf2\\\xf0\xa2\x8ah\xb6r\x11\xab\xe0\xb0|s\x1c\x0b\xaa\xf7\x84~y\xfbox\xfb\x96\x889X\x80\xcc4\xf6\x16\x1e\x92\x14\xb8\x9d\xd04\xccA\xc6X`\xeb\xae\x13\xf6\xe5\xba\x13\x1d\x14i\xe8\xcd'
    the_hex_from = the_msg.hex()
    #二进制文件转为hexto10
    the_length = len(the_hex_from)
    i = 0
    while i+2 < the_length:
        the_hex = the_hex_from[i:i+2]
        print(int(the_hex, 16))
        i = i+2



    #  Go 语言解密出来的16进制数
    mes = "436f6e67726174756c6174696f6e732120596f752068617665207375636365737366756c6c7920736f6c766564207468652070757a7a6c652120476f6f64206a6f6221"

    # ANS !!!!!!!!!!!
    print(Converter.to_ascii(mes))


