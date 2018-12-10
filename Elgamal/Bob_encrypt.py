""""""
from my_strong_treasure import Decode
from big_number import BigNumber
import hashlib
import random
import string
random_seed = 100  # 控制随机取的整数

class BobEncrypt:

    def __init__(self, public_key, signature):
        self.public_key = public_key
        pk = public_key.split(',')
        self.p = int(pk[0], 16)
        self.g = int(pk[1], 16)
        self.ya = int(pk[2], 16)
        sig = signature.split(',')
        self.sig_r = int(sig[0], 16)
        self.sig_s = int(sig[1], 16)
        # if not self.verify_sig():
        #     print("verify error!!!")
        #     exit()
        # else:
        #     print("verify pass!!!")


    def encrypt_origin_text(self, message):
        """
        :param message: 传递的明文 e.g. "fangzhou"
                        使用随机流密码加密密文
        """
        # this is the encrypt message
        self.message = message

        # this stream key is a hex string type
        self.stream_key = Decode.get_hex_code(self.genRandomString(len(message)))
        # 流密码的十进制int类型
        self.stream_key_num_form = int(self.stream_key, 16)

        # cipher_messages is the hex type string, so when decrypt it does not need to de transformed
        self.cipher_messges = Decode.Two_string_OXR(Decode.get_hex_code(message),
                                                    self.stream_key)
        return self.cipher_messges

    def encrypt_stream_key(self):
        """
        利用私钥加密流密码的key
        elgamal的加密方式，密文由两个部分组成
        返回(c1, c2)
        :return:
        """
        random_k = random.randint(2, random_seed)
        k = BigNumber.get_quick_mi_mod(self.ya, random_k, self.p)
        self.cipher_key_c1 = BigNumber.get_quick_mi_mod(self.g, random_k, self.p)
        self.cipher_key_c2 = (k * self.stream_key_num_form) % self.p
        self.cipher_key = hex(self.cipher_key_c1)[2:] + "," + hex(self.cipher_key_c2)[2:]
        return self.cipher_key

    @staticmethod
    def genRandomString(slen=10):
        """
        :param slen: 生成的字符串的长度
        :return:  一个随机的字符串
        """
        return ''.join(random.sample(string.ascii_letters + string.digits, slen))

    def verify_sig(self):
        """
        验证签名
        :return:
        """
        if not (0 < self.sig_r < self.p and 0 < self.sig_s < (self.p-1)):
            return False
        if pow(self.g, int(hashlib.sha256(self.public_key.encode("ascii")).hexdigest(), 16), self.p) != ((pow(self.ya, self.sig_r) * pow(self.sig_r, self.sig_s)) % self.p):
            return False
        return True
