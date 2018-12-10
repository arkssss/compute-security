"""
author : 方舟
email : 522500442@qq.com
for : 密码学作业

消息的接受方
产生密钥
解密消息
"""
from my_strong_treasure import Decode
import random
import hashlib
from big_number import BigNumber
hex_seed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']  # 十六进制的种子
random_seed = 100  # 控制随机取的整数


class AliceDecrypt:

    def __init__(self):
        self.genskandpk()


    def get_pk(self):
        """
        外界获得公钥的方法
        和签名
        :return:
        """
        self.send_pk = hex(self.p)[2:] + "," + hex(self.g)[2:] + "," + hex(self.Ya)[2:]
        self.send_sig = self.gen_sig(self.send_pk)
        return self.send_pk, self.send_sig


    def genskandpk(self):
        """
        开始计算公钥和私钥
        :return:
        """
        # 注意在类里 q, p 都是一个int类型 ，而非string
        # 获得 p ,g
        self.p, self.g = BigNumber.get_bigprime_generator(256)
        self.sk = random.randint(2, random_seed)
        self.Ya = BigNumber.get_quick_mi_mod(self.g, self.sk, self.p)

    def decrypt(self, cipher_text, cipher_key):
        """
        :return: 明文
        """
        cipher_key_str = cipher_key.split(',')
        c1 = int(cipher_key_str[0], 16)
        c2 = int(cipher_key_str[1], 16)
        K = BigNumber.get_quick_mi_mod(c1, self.sk, self.p)
        # K = (c1 ** self.sk) % self.p
        stream_key = hex((c2 * BigNumber.get_inverse(K, self.p)) % self.p)[2:]

        # 返回明文
        return Decode.StringToASCII(Decode.Two_string_OXR(stream_key, cipher_text))

    def gen_sig(self, message):
        """
        对发送的消息message进行数字签名
        :return: (r, s) 的签名对
        """
        for i in range(2, self.p - 1):
            if BigNumber.gcd(i, self.p - 1) == 1:
                k = i
                r = BigNumber.get_quick_mi_mod(self.g, k, self.p)
                # print(hashlib.sha256(message.encode("ascii")).hexdigest())
                s = ((int(hashlib.sha256(message.encode("ascii")).hexdigest(), 16) - self.sk * r) * BigNumber.get_inverse(k, self.p)) % (self.p - 1)
                # s == 0 则重新选取
                if not s:
                    continue
                return hex(r)[2:] + "," + hex(s)[2:]








