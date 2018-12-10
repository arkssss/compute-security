from Alice_decrypt import AliceDecrypt
from Bob_encrypt import BobEncrypt


# alice 产生pk & sk
my_alice = AliceDecrypt()
the_pk, sig = my_alice.get_pk()

# bob 加密text 和 stream_key
# message = "fangzhou"
message = input("please input the message you want to encrypt\n")


print("your signature to be verified is \n" + sig)
# 构造函数里面便有验证signature
my_bob = BobEncrypt(the_pk, sig)

# 到这一步说明验证通过
cipher_text = my_bob.encrypt_origin_text(message)
print("your cipher text is \n" + cipher_text)
cipher_key = my_bob.encrypt_stream_key()
print("you cipher_key is \n" + cipher_key)


# 解密
the_message = my_alice.decrypt(cipher_text, cipher_key)
print("your message is : \n" + the_message)















