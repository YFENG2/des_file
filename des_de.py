#_*_coding:utf-8_*_
#!/usr/bin/env python
#Filename:des.py

from desstruct import *
import re

__all__=['desdecode']
class DES():
	
	def __init__(self):
		pass
	
	def decode(self,string,key,key_len,string_len):
		output=""
		trun_len=0
		num=0
		
		
		code_string=self._functionCharToA(string,string_len)
		
		code_key=self._getkey(key,key_len)
				
		
		
		real_len=(key_len/16)+1 if key_len%16!=0 else key_len/16
		trun_len=string_len*4
	
		for i in range(0,trun_len,64):
			run_code=code_string[i:i+64]
			run_key=code_key[num%real_len]

			
			run_code= self._codefirstchange(run_code)
			
			
			for j in range(16):
				
				code_r=run_code[32:64]
				code_l=run_code[0:32]
				
					
				run_code=code_r
				
				
				code_r= self._functionE(code_r)
				
				
				key_y=run_key[15-j]

				
				code_r= self._codeyihuo(code_r,key_y)
				
				
				code_r= self._functionS(code_r)
				
				
				code_r= self._functionP(code_r)
				
				
				code_r= self._codeyihuo(code_l,code_r)
				
				run_code+=code_r
			num+=1
			
			
			code_r=run_code[32:64]
			code_l=run_code[0:32]
			run_code=code_r+code_l
			
			
			output+=self._functionCodeChange(run_code)
		return output
	
	
	def _getkey(self,key,key_len):
		
		
		code_key=self._functionCharToA(key,key_len)
		
		a=['']*16
		real_len=(key_len/16)*16+16 if key_len%16!=0 else key_len

		b=['']*(real_len/16)
		for i in range(real_len/16):
			b[i]=a[:]
		num=0
		trun_len=4*key_len
		for i in range(0,trun_len,64):
			run_key=code_key[i:i+64]
			run_key= self._keyfirstchange(run_key)
			for j in range(16):
				key_l=run_key[0:28]
				key_r=run_key[28:56]
				key_l=key_l[d[j]:28]+key_l[0:d[j]]
				key_r=key_r[d[j]:28]+key_r[0:d[j]]
				run_key=key_l+key_r
				key_y= self._functionKeySecondChange(run_key)
				b[num][j]=key_y[:]
			num+=1

		return b	
		
		 							
	def _codeyihuo(self,code,key):
		code_len=len(key)
		return_list=''
		for i in range(code_len):
			if code[i]==key[i]:
				return_list+='0'
			else:
				return_list+='1'
		return return_list

			 							
	def _codefirstchange(self,code):
		changed_code=''
		for i in range(64):
			changed_code+=code[ip[i]-1]
		return changed_code
		
	
	def _keyfirstchange (self,key):
		changed_key=''
		for i in range(56):
			changed_key+=key[pc1[i]-1]
		return changed_key
	
	
	def _functionCodeChange(self, code):
		return_list=''
		for i in range(16):
			list=''
			for j in range(4):
				list+=code[ip_1[i*4+j]-1]
			return_list+="%x" %int(list,2)
		return return_list
	
		
	def _functionE(self,code):
		return_list=''
		for i in range(48):
			return_list+=code[e[i]-1]
		return return_list		
	
		
	def _functionP(self,code):
		return_list=''
		for i in range(32):
			return_list+=code[p[i]-1]
		return return_list

		
	def _functionS(self, key):
		return_list=''
		for i in range(8):
			row=int( str(key[i*6])+str(key[i*6+5]),2)
			raw=int(str( key[i*6+1])+str(key[i*6+2])+str(key[i*6+3])+str(key[i*6+4]),2)
			return_list+=self._functionTos(s[i][row][raw],4)

		return return_list
	
	
	def _functionKeySecondChange(self,key):
		return_list=''
		for i in range(48):
			return_list+=key[pc2[i]-1]
		return return_list
	
	
	def _functionCharToA(self,code,lens):
		return_code=''
		lens=lens%16
		for key in code:
			code_ord=int(key,16)
			return_code+=self._functionTos(code_ord,4)
		
		if lens!=0:
			return_code+='0'*(16-lens)*4
		return return_code
	
	
	def _functionTos(self,o,lens):
		return_code=''
		for i in range(lens):
			return_code=str(o>>i &1)+return_code
		return return_code


def tohex(string):
	return_string=''
	for i in string:
		return_string+="%02x"%ord(i)
	return return_string
		
def tounicode(string):
	return_string=''
	string_len=len(string)
	for i in range(0,string_len,2):
		return_string+=chr(int(string[i:i+2],16))
	return return_string
	

def desdecode(from_code,key):
	key=tohex(key)

	des=DES()
	
	key_len=len(key)
	string_len=len(from_code)
	if string_len%16!=0:
		return False
	if string_len<1 or key_len<1:
		return False

	key_code= des.decode(from_code,key,key_len,string_len)
	return tounicode(key_code)
	
#test
if __name__  == '__main__':
	print("DES decrypt\n")
	#please input your file path which you want to encrypt.
	path="/home/fg/0417liyaofeng.tar"
	f = open(path, "rb")
	ciper=f.read()
	f.close()
	key=raw_input("please input the key:")
	f1 = open(path, "wb")
	f1.write(desdecode(ciper,key))
	f1.close()
	print desdecode(ciper,key)
	k=raw_input("enter")


