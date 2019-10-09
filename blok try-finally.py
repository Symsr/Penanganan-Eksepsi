def main():
 try:
	 
	f = open("data.txt", "w")
	
	try:
		
		f.write("Pemprograman Python")
	finally:
		f.close()
	except IOError;
		print("\nERROR: File tidak dapat " + "dibuka/ditulis")

if __name__ == "__main__":
	main()
