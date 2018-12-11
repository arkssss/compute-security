package main 
import "fmt"
import "crypto/rc4"
func main() {


	 var key []byte = []byte{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15 ,16} //初始化用于加密的KEY 
     fmt.Println(key)
     rc4obj1, _ := rc4.NewCipher(key) //返回 Cipher
     // rc4str1 := []byte{d9 a8 a2 fd 12 fc 6a 82 de f2 5c f0 a2 8a 68 b6}  //需要加密的字符串
     rc4str1 := []byte{217,
168,
162,
253,
18,
252,
106,
130,
222,
242,
92,
240,
162,
138,
104,
182,
114,
17,
171,
224,
176,
124,
115,
28,
11,
170,
247,
132,
126,
121,
251,
111,
120,
251,
150,
136,
57,
88,
128,
204,
52,
246,
22,
30,
146,
20,
184,
157,
208,
52,
204,
65,
198,
88,
96,
235,
174,
19,
246,
229,
186,
19,
29,
20,
105,
232,
}	
     plaintext := make([]byte, len(rc4str1)) //
     rc4obj1.XORKeyStream(plaintext, rc4str1)


	 fmt.Println(plaintext)
     stringinf1 := fmt.Sprintf("%x\n", plaintext) //转换字符串
  	 fmt.Println(stringinf1)



  // 	 var key []byte = []byte("fd6cde7c2f4913f22297c948dd530c84") //初始化用于加密的KEY 
  // 	 fmt.Println(key)
  //    rc4obj1, _ := rc4.NewCipher(key) //返回 Cipher
  //    rc4str1 := []byte("xiaowangnidayede")  //需要加密的字符串
  //    plaintext := make([]byte, len(rc4str1)) //
  //    rc4obj1.XORKeyStream(plaintext, rc4str1)
  // 	 // stringinf1 := fmt.Sprintf("%x\n", plaintext) //转换字符串
	 // // fmt.Println(stringinf1)

	 // // var key []byte = []byte("fd6cde7c2f4913f22297c948dd530c84") //初始化用于加密的KEY 
  //    rc4obj2, _ := rc4.NewCipher(key) //返回 Cipher
  //    rc4str2 := []byte(plaintext)  //需要加密的字符串
  //    plaintext2 := make([]byte, len(rc4str2)) //
  //    rc4obj2.XORKeyStream(plaintext2, rc4str2)        
  //    stringinf2 := fmt.Sprintf("%x\n", plaintext2) //转换字符串

  //    fmt.Println(stringinf2)


}