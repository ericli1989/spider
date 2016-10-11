#-*- coding: utf-8 -*-

import math

class get_g_tk:
	
	def calc_g_tk(self, str):
		#hash=5381
		hash=2767962132
		str_len=len(str)
		for i in range(0, str_len):
			temp=str[i]
			print ord(temp)
			hash += (hash << 5) + ord(temp); 	
		print hash & 0x7fffffff

	def start(self):
		print "begin"	
		print u"请输入skey值"
		str=raw_input()
		self.calc_g_tk(str)	


get_temp_g_tk = get_g_tk()
get_temp_g_tk.start()
	


