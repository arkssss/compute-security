class Decode:
    def __init__(self, c1, c2):
        """输入两端字符串形式的加密文c1 c2"""
        self.c1 = c1
        self.c2 = c2

    @staticmethod
    def StringToASCII(StringText):
        """将string中的16进制 转化为16进制所对应的ascII字符"""
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
                AsciiString += Decode.TwoBit_To_Hex(tmp)
                HexFlag = 0
            index += 1
        return AsciiString


    @staticmethod
    def TwoBit_To_Hex(stringBit):
        """将stringbit转为十六进制  'ab'==>0xab """
        FirstBit = stringBit[0]
        SecondBit = stringBit[1]
        firstHex = Decode.Bit_To_Hex(FirstBit) * 0x10
        SecondBit = Decode.Bit_To_Hex(SecondBit)
        return chr(firstHex+SecondBit)



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
    def get_hex_code(StringText):
        """得到StringText的Ascii码的十六进制 StringToASCII的反过程"""
        length = len(StringText)
        ASCiiCode = ""
        index = 0
        while index < length:
            ASCiiCode += Decode.get_hex_by_bit(StringText[index])
            index += 1
        return ASCiiCode

    @staticmethod
    def get_hex_by_bit(OneChar):
        """已知OneChar为字符，得到他的ASCii码的十六进制"""
        return hex(ord(OneChar))[2:]

    @staticmethod
    def Two_string_OXR(StringOne, StringTwo):
        """两个字符串形式的十六进行异或 得到较短的"""
        length1 = len(StringOne)
        length2 = len(StringTwo)
        if length1 > length2:
            length = length2
        else:
            length = length1
        res = ""
        index = 0
        while index < length:
            res += Decode.XOR_Two_Bit(StringOne[index], StringTwo[index])
            index += 1
        return res

    @staticmethod
    def XOR_Two_Bit(BitOne, BitTwo):
        """异或两十六进制位 eg 'a' XOR '2'  """
        return hex(Decode.Bit_To_Hex(BitOne) ^ Decode.Bit_To_Hex(BitTwo))[2:]
