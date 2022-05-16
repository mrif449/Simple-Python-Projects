import os
from cryptography.fernet import Fernet
data = []
for item in os.listdir():
	if item == "ransomeware.py" or item == "key.txt" or item == "unlocker.py":
		continue
	else:	
			data.append(item)
with open("key.txt","rb") as key:
	locker = key.read()
for item in data:
	with open(item,"rb") as content:
		elements = content.read()
	decrypted = Fernet(locker).decrypt(elements)
	with open(item,"wb") as content:
		content.write(decrypted)
print("Congratulations, your files are decrypted successfully!!")
print("I have decrypted following files:")
for x in range(len(data)):
	print(f"{str(x+1)}. {data[x]}")