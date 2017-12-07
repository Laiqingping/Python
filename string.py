def replacestr():
	s = "23abc324adb99fsodfjojkf03"
	s=s.replace("abc","ooo")
	print(s)
def deleteother():
	s= "32abc34abc3433adc8989fsjjsjdflkasjd"
	first = s.find("abc")
	s1 = s[first+3:]
	print (s1)
	s2= s[0:first+3]
	s1=s1.replace("adc","")
	print(s2+s1)
if __name__=="__main__":
	#replacestr()
	deleteother()