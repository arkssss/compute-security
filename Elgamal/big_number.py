"""
大数运算类
"""
from rsa.prime import getprime  # 生成素数的函数
from rsa.common import inverse
from Crypto.PublicKey.ElGamal import generate
import random
class BigNumber:

    @staticmethod
    def get_quick_mi_mod(a, b, mod):
        """
        返回 a**b % mod
        :param a:
        :param b:
        :param mod:
        :return:
        """
        return pow(a, b, mod)

    @staticmethod
    def get_primer(nbits):
        """
        返回一个nbits的素数
        """
        return getprime(nbits)

    @staticmethod
    def get_inverse(a, p):
        """
        p乘法群里取逆运算
        :param a:
        :param p:
        :return:
        """
        return inverse(a, p)

    @staticmethod
    def get_bigprime_generator(nbits):
        """
        获得一个nbits的素数， 和一个生成元
        :return:
        """
        obj = generate(nbits, randfunc=None)
        return int(obj.p), int(obj.g)

    @staticmethod
    def get_generator(primer):
        """
        找到一个素数的生成元
        :param primer:
        :return:
        """
        # Generate generator g
        while 1:
            # Choose a square residue; it will generate a cyclic group of order q.
            g = pow(random.randint(2, primer), 2, primer)

            if g in (1, 2):
                continue

            # Discard g if it divides p-1 because of the attack described
            if (primer - 1) % g == 0:
                continue

            # g^{-1} must not divide p-1 because of Khadir's attack
            ginv = BigNumber.get_inverse(g, primer)
            if (primer - 1) % ginv == 0:
                continue

            # Found
            return g

    @staticmethod
    def gcd(p, q):
        """Returns the greatest common divisor of p and q
        gcd(48, 180)
        12
        """
        while q != 0:
            (p, q) = (q, p % q)
        return p






