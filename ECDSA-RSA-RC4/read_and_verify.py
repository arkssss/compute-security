"""
提取1000条记录，并且解出通过验证的记录
"""

import hashlib
from ecdsa import VerifyingKey, ellipticcurve, util, curves, keys
# 构造特殊的curve 类
x = 0xA374F7774070CD8BECCDD5B01450FFBC0033EE5FFBFEC7829C10DDD1
y = 0xF484F9AF3B9DD12C93F5DA7971333C3A0DCDBD20865CCE59145D9180
_r = 26959946667150639794667015087019625940457807714424391721682722368061   # order
# 构造公钥的pk(在给定的点的情况下)
public_point = ellipticcurve.Point(curves.NIST224p.curve, x, y, _r)
# 构造vk用于验证
vk = VerifyingKey.from_public_point(public_point, curve=curves.NIST224p, hashfunc=hashlib.sha256)
the_order = vk.pubkey.order


def read_rc4():
    with open("record/RC4KeyAndSignature.txt") as file_obj:
        the_lines = file_obj.readlines()
    return the_lines


def get_ci():
    """度读取ci文件"""
    records = read_rc4()
    for record in records:
        spilt_record = record.split(',')
        c = spilt_record[0]
        r_int = int(spilt_record[1], 16)
        s_int = int(spilt_record[2], 16)
        sig = util.sigencode_string(r_int, s_int, the_order)
        try:
            vk.verify(sig, bytearray.fromhex(c))
        except keys.BadSignatureError:
            continue
        print("the break Ci is:" + c)
        break


def read_rsa():
    """读取rsa文件"""
    with open("record/RSAKeyAndSignature.txt") as file_obj:
        the_lines = file_obj.readlines()
    return the_lines


def get_sk_and_pk():
    """读取sk和pk文件"""
    records = read_rsa()
    for record in records:
        spilt_record = record.split(',')
        n = spilt_record[0]+','
        e = spilt_record[1]+','
        d = spilt_record[2]+','
        # if len(d) % 2:
        #     d = "0" + spilt_record[2]
        p = spilt_record[3]+','
        q = spilt_record[4]
        r_int = int(spilt_record[5], 16)
        s_int = int(spilt_record[6], 16)
        # 构造签名
        mes = n+e+d+p+q
        sig = util.sigencode_string(r_int, s_int, the_order)
        try:
            vk.verify(sig, mes.encode("ascii"))
        except keys.BadSignatureError:
            continue
        print("n:" + n)
        print("e:" + e)
        print("d:" + d)
        print("p:" + p)
        print("q:" + q)
        break


if __name__ == "__main__":
    # verify the sig 
    get_ci()
    get_sk_and_pk()





