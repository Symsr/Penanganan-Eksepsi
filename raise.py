class ContohAbstrak(object):
	def __init__(self):
		raise Exception("Kelas tidak dapat "+"diintansiasi")
obj = ContohAbstrak()
Traceback (most recent call last):
	File "<pyshell#3>", line 1, in <module>
		obj = ContohAbstrak()
	File "D:/Praktikum/Pemprograman lanjut/raise.py", line 3, in __init__ raise Exception("Kelas tidak dapat "+"diintansiasi")
Exception: Kelas tidak dapat di intansiasi
