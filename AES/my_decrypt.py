from Crypto.Cipher import AES


class MyDecrypt:
    def __init__(self, key, cipher_text, IV_len = 16):
        """CBC模式的下的AES
            此时知道 key
            知道 cipher_text
            要求以CBC格式的解码
            IV_len为在密文首添加的IV长度, 单位为byte
        """
        self.key = key
        self.byte_key = bytes.fromhex(key)
        self.AES_mode = AES.MODE_ECB
        self.cipher_test = cipher_text
        # 加密
        self.AES = AES.new(self.byte_key, self.AES_mode)
        self.key_len = len(key)
        self.IV_len = IV_len
        # 以十六进制表示的时候，1byte = 2 位十六进制
        self.IV_len_hex = self.IV_len * 2
        self.IV_text = self.cipher_test[:self.IV_len_hex]
        # real_text为不加IV的密文部分
        self.real_text = self.cipher_test[self.IV_len_hex:]
        # block_times为密文分块的数量
        # self.block_times = int(len(self.real_text) / len(self.key))
        if float(len(self.real_text)) / len(self.key) > int(len(self.real_text) / len(self.key)):
            self.block_times = int(len(self.real_text) / len(self.key)) + 1
        else:
            self.block_times = int(len(self.real_text) / len(self.key))

        self.blocks = []
        #加密
        self.aes = AES.new(str.encode(self.key), AES.MODE_ECB)
        # 一个block的长度等于key的长度
        for i in range(0, self.block_times):
            temp_block = self.real_text[i * self.key_len: (i+1) * self.key_len]
            self.blocks.append(temp_block)
        # print(self.IV_text)
        # print(self.blocks[0])

    def ASE_TO_BE_FINSHED_CBC(self, message):
        """
        此为待实现的AES加密函数
        传入一个key, message
        此时传入的message为str类型的，需要以byte的格式进行解密
        且解密之后返回一个十六进制类型的str
        返回一个加密的映射
        """
        decrypte_message = self.AES.decrypt(bytes.fromhex(message)).hex()
        return decrypte_message
            # return str(base64.b64encode(self.aes.encrypt(str.encode(message))), encoding='utf-8')

    def ASE_TO_BE_FINSHED_CTR(self, message):
        """
        CTR模式为对message进行加密操作，而非解密
        :param message:
        :return:
        """
        decrypte_message = self.AES.encrypt(bytes.fromhex(message)).hex()
        return decrypte_message

    def get_CBC_message(self):
        """以CBC的方式解密
        IV XOR C[]
        """
        message = ""
        index = 0
        xor_text = self.IV_text
        while index < self.block_times:
            # print(xor_text)
            # print(self.ASE_TO_BE_FINSHED(self.blocks[index]))
            message += self.XOR_Two_String(self.ASE_TO_BE_FINSHED_CBC(self.blocks[index]), xor_text)
            xor_text = self.blocks[index]
            index += 1
        return self.Hex_to_readable(message)

    def get_CTR_message(self):
        """
        以CTR的方式进行解密
        IV 隔一个加一
        :return:
        """
        message = ""
        index = 0
        Xor_text = self.IV_text
        while index < self.block_times:
            message += self.XOR_Two_String(self.ASE_TO_BE_FINSHED_CTR(Xor_text), self.blocks[index])
            Xor_text = self.increasement_IV(Xor_text)
            index += 1
        return self.Hex_to_readable(message)

    @staticmethod
    def increasement_IV(string):
        """
        :param string: 十六进制的字符串
        :return: 该字符串加一之后的结果
        """
        length = len(string)
        index = length - 1
        while index >= 0:
            if string[index] != 'f':
                #直接返回加一的结果
                tmp_list = list(string)
                tmp_list[index] = hex(MyDecrypt.Bit_To_Hex(string[index]) + 0x1)[2:]
                string = ''.join(tmp_list)
                return string
            else:
                tmp_list = list(string)
                tmp_list[index] = hex(MyDecrypt.Bit_To_Hex(string[index]) + 0x1)[2:]
                string = ''.join(tmp_list)
                index -= 1
        return string


    @staticmethod
    def Bit_To_Hex(Bit):
        """ 'a'==> 0xA  """
        if Bit == 'a':
            return 0xa
        elif Bit == 'b':
            return 0xb
        elif Bit == 'c':
            return 0xc
        elif Bit == 'd':
            return 0xd
        elif Bit == 'e':
            return 0xe
        elif Bit == 'f':
            return 0xf
        else:
            return int(Bit)


    @staticmethod
    def XOR_Two_Bit(BitOne, BitTwo):
        """异或两十六进制位 eg 'a' XOR '2'  """
        return hex(MyDecrypt.Bit_To_Hex(BitOne) ^ MyDecrypt.Bit_To_Hex(BitTwo))[2:]

    @staticmethod
    def XOR_Two_String(StringOne, StringTwo):
        """异或两段字符串,返回十六进制的字符串结果"""
        length1 = len(StringOne)
        length2 = len(StringTwo)
        if length1 > length2:
            length = length2
        else:
            length = length1
        res = ""
        index = 0
        while index < length:
            res += MyDecrypt.XOR_Two_Bit(StringOne[index], StringTwo[index])
            index += 1
        return res

    @staticmethod
    def TwoBit_To_Hex(stringBit):
        """将stringbit转为十六进制  'ab'==>0xab """
        FirstBit = stringBit[0]
        SecondBit = stringBit[1]
        firstHex = MyDecrypt.Bit_To_Hex(FirstBit) * 0x10
        SecondBit = MyDecrypt.Bit_To_Hex(SecondBit)
        return chr(firstHex+SecondBit)

    @staticmethod
    def Hex_to_readable(StringText):
        """传入一个十六进制形式的ASCII码, 返回一段可读的文字"""
        length = len(StringText)
        index = 0
        AsciiString = ""
        tmp = ""
        HexFlag = 0
        while index < length:
            if not HexFlag:
                tmp = ""
                tmp += StringText[index]
                HexFlag += 1
            else:
                tmp += StringText[index]
                AsciiString += MyDecrypt.TwoBit_To_Hex(tmp)
                HexFlag = 0
            index += 1
        return AsciiString