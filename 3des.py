pi=100005

salt_const=b"$ez*}-d3](%d%$#*!)$#%s45le$*fhucdivyanshu75456dgfdrrrrfgfs^"

#importing libraries
from crypto.Cipher import DES
from crypto.Hash import SHA256
from getpass import getpass
from crypto.Protocol.KDF import PBKDF2



#encrypting function
def encryptor(path):
	#opening the image file
	try:
		with open(path, 'rb') as imagefile:#Open the file in binary mode  ,Opens a file for reading
			image=imagefile.read()
			
		#padding	
		while len(image)%8!=0:
			image+=b" "# 
	except:
		print("Error loading the file, make sure file is in same directory, spelled correctly and non-corrupted")
		exit()
	
	#hashing original image in SHA256	
	hash_of_original=SHA256.new(data=image)
	
	# 64 bit key entry in as password
	
	#Inputting Keys
	key_enc=getpass(prompt="		      Enter minimum 8 character long password:")
	#Checking if key is of invalid length
	while len(key_enc)<8:
		key_enc=getpass(prompt="		      Invalid password! Enter atleast 8 character password:")
	
	key_enc_confirm=getpass(prompt="		       Enter password again:")
	while key_enc!=key_enc_confirm:
		print("Key Mismatch.Try again.")
		key_enc=getpass(prompt="		      Enter 8 character long password:")
	
		#Checking if key is of invalid length
		while len(key_enc)<8:
			key_enc=getpass(prompt="		      Invalid password! Enter atleast 8 character password:")
		key_enc_confirm=getpass(prompt="		       Enter password again:")
	
	
	#Salting and hashing password
	key_enc=PBKDF2(key_enc,salt_const,48,count=pi)
	#A salt is a random string added to the plaintext password and hashed together to generate the irreversible hash

	
	#Encrypting using triple 3 key DES	
	print("			encrypting...")	
	try:
		
		cipher1=DES.new(key_enc[0:8],DES.MODE_CBC,key_enc[24:32])
		ciphertext1=cipher1.encrypt(image)
		cipher2=DES.new(key_enc[8:16],DES.MODE_CBC,key_enc[32:40])
		ciphertext2=cipher2.decrypt(ciphertext1)
		cipher3=DES.new(key_enc[16:24],DES.MODE_CBC,key_enc[40:48])
		ciphertext3=cipher3.encrypt(ciphertext2)
		print("			!!!ENCRYPTION SUCCESSFUL!!!")
	except:
		print("			Encryption failed...Possible causes:Library not installed properly/low device memory/Incorrect padding or conversions")
		exit()
	
	#Adding hash at end of encrypted bytes
	ciphertext3+=hash_of_original.digest()

	
	#Saving the file encrypted
	try:
		dpath="encrypted_"+path
		with open(dpath, 'wb') as image_file:
    			image_file.write(ciphertext3)
		print("			Encrypted Image Saved successfully as filename "+dpath)
    		
		
	except:
		temp_path=input("			Saving file failed!. Enter alternate name without format to save the encrypted file. If it is still failing then check system memory")
		try:
			dpath=temp_path+path
			dpath="encrypted_"+path
			with open(dpath, 'wb') as image_file:
    				image_file.write(ciphertext3)
			print("			Encrypted Image Saved successfully as filename "+dpath)
			exit()
		except:
			print("			Failed....Exiting...")
			exit()

#decrypting function
def decryptor(encrypted_image_path):
	
	try:
		with open(encrypted_image_path,'rb') as encrypted_file:
			encrypted_data_with_hash=encrypted_file.read()
			
	except:
		print("			Unable to read source cipher data. Make sure the file is in same directory...Exiting...")
		exit()
	
	
	#Inputting the key
	key_dec=getpass(prompt="		      Enter password:")
	
	
	#extracting hash and cipher data without hash
	extracted_hash=encrypted_data_with_hash[-32:]#first 32 bit extracted
	encrypted_data=encrypted_data_with_hash[:-32]#last 32 bit extracted

	
	#salting and hashing password
	key_dec=PBKDF2(key_dec,salt_const,48,count=pi)
	

	#decrypting using triple 3 key DES
	print("			Decrypting...")
	try:
		
		cipher1=DES.new(key_dec[16:24],DES.MODE_CBC,key_dec[40:48])
		plaintext1=cipher1.decrypt(encrypted_data)
		cipher2=DES.new(key_dec[8:16],DES.MODE_CBC,key_dec[32:40])
		plaintext2=cipher2.encrypt(plaintext1)
		cipher3=DES.new(key_dec[0:8],DES.MODE_CBC,key_dec[24:32])
		plaintext3=cipher3.decrypt(plaintext2)
		
		
	except:
		print("			Decryption failed...Possible causes:Library not installed properly/low device memory/Incorrect padding or conversions")
		
	
	
	
	
	#hashing decrypted plain text
	hash_of_decrypted=SHA256.new(data=plaintext3)

	
	#matching hashes
	if hash_of_decrypted.digest()==extracted_hash:
		print("Password Correct !!!")
		print("			DECRYPTION SUCCESSFUL!!!")
	else:
		print("Incorrect Password!!!")
		exit()
		
		
		
	#saving the decrypted file	
	try:
		epath=encrypted_image_path
		if epath[:10]=="encrypted_":
			epath=epath[10:]
		epath="decrypted_"+epath
		with open(epath, 'wb') as image_file:
			image_file.write(plaintext3)
		print("			Image saved successully with name " + epath)
		print("			Note: If the decrypted image is appearing to be corrupted then password may be wrong or it may be file format error")
	except:
		temp_path=input("			Saving file failed!. Enter alternate name without format to save the decrypted file. If it is still failing then check system memory")
		try:
			epath=temp_path+encrypted_image_path
			with open(epath, 'wb') as image_file:
				image_file.write(plaintext3)
			print("			Image saved successully with name " + epath)
			print("			Note: If the decrypted image is appearing to be corrupted then password may be wrong or it may be file format error")
		except:
			print("			Failed! Exiting...")
			exit()

#Documentations
print("----------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------- ENCRYPTOR-DECRYPTOR TOOL Using Triple-DES--------------------------------------------")
print("")
print("")
#--------------------------------------MAIN PROGRAM-----------------------------------------------
#Mode selection
try:
	choice=int(input("		Press 1 for Encryption || 2 for Decryption: "))
	while choice!=1 and choice!=2:
		choice=int(input("						Invalid Choice! Try Again:"))
except:
	print("						Error, please provide valid Input")
	exit()



if choice==1:
#Encryption Mode, function call
	path=input("		Enter file's name to be encypted:")
	encryptor(path)
		


else:
#Decryption mode, function call
	encrypted_image_path=input("		Enter file's name to decrypted:")
	decryptor(encrypted_image_path)

print("")
print("")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------")
