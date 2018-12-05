from my_decrypt import MyDecrypt


# 第一段CBC
key_one = "140b41b22a29beb4061bda66b6747e14"
cipher_text_one = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e0' \
                  '08a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
the_CBC_one = MyDecrypt(key_one, cipher_text_one)
print(the_CBC_one.get_CBC_message())

# 第二段CBC
key_two = "140b41b22a29beb4061bda66b6747e14"
cipher_text_two = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249" \
                  "de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
the_CBC_two = MyDecrypt(key_two, cipher_text_two)
print(the_CBC_two.get_CBC_message())

# 第三段CTR
key_three = "36f18357be4dbd77f050515c73fcf9f2"
cipher_text_three = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1" \
                    "cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
the_CBC_three = MyDecrypt(key_three, cipher_text_three)
print(the_CBC_three.get_CTR_message())


# 第四段CTR
key_four = "36f18357be4dbd77f050515c73fcf9f2"
cipher_text_four = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
the_CBC_four = MyDecrypt(key_four, cipher_text_four)
print(the_CBC_four.get_CTR_message())



# test
# IV = "4ca00ff4c898d61e1edbf1800618fb28"
# block_0 = "28a226d160dad07883d04e008a7897ee"
# key = "140b41b22a29beb4061bda66b6747e14"
#
#
# bytes_block_0 = bytes.fromhex(block_0)
# bytes_key = bytes.fromhex(key)
# print(bytes_key)
# print(bytes_key + bytes_key.fromhex("01"))
#
# the_AES = AES.new(bytes_key, AES.MODE_ECB)
# res = the_AES.decrypt(bytes_block_0).hex()
#
# mes = CbcMode.XOR_Two_String(res, IV)
#
# print(CbcMode.Hex_to_readable(mes))
#
# a = "123"
# print(type(a[2]))
# a[2] = '1'
# # a[1] = hex(0x9 + 1)[2:]
#
# print(type(a))


#m1[0] = XOR(IV, F(block_0, key))