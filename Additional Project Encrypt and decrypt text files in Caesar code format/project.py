import os
def EncryptTheSentence(sen, key=1):
	if sen != "" and (1 <= key <= 25):
		alpha_lower = "abcdefghijklmnopqrstuvwxyz"
		alpha_lower += alpha_lower[:key+1]
		alpha_upper = alpha_lower.upper()
		alpha_upper += alpha_upper[:key+1]
		result = ""
		if len(sen) == 2:
			result += sen
		else:
			if sen[:-2] == "\n":
				sen = sen[:-2]
			for letter in sen:
				if letter in alpha_lower:
					letter = alpha_lower[alpha_lower.index(letter) + key]
					result += letter
				elif letter in alpha_upper:
					letter = alpha_upper[alpha_upper.index(letter) + key]
					result += letter
				else:
					result += letter
			if sen[:-2] == "\n":
				result += '\n'
		return result
	return ""
def DecryptTheSentence(sen, key=1):
	if sen != "" and (1 <= key <= 25):
		key *= -1
		result = ""
		if len(sen) == 2:
			result += sen
		else:
			if sen[:-2] == "\n":
				sen = sen[:-2]
			for letter in sen:
				alpha_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
				alpha_lower = alpha_lower[:key+1] + alpha_lower
				alpha_upper = alpha_lower.upper()
				alpha_upper = alpha_upper[:key+1] + alpha_upper
				if letter in alpha_lower:
					letter = alpha_lower[alpha_lower.index(letter) + key]
					result += letter
					alpha_lower = alpha_lower.replace(alpha_lower[alpha_lower.find(letter,25):], "")
				elif letter in alpha_upper:
					letter = alpha_upper[alpha_upper.index(letter) + key]
					result += letter
					alpha_upper = alpha_upper.replace(alpha_upper[alpha_upper.find(letter,25):], "")
				else:
					result += letter
			if sen[:-2] == "\n":
				result += '\n'
		return result
	return ""
wellcom = "\tWelcome To Encrypt And Decrypt text Files With Caesar Cipher"
path = os.getcwd()
list_files = os.listdir(path)
print "=" * (len(wellcom) + 7)
print wellcom
print "=" * (len(wellcom) + 7)
status = "Error"
while status == "Error":
	print "Please Enter The Number"
	print "\t[1] To Encrypt The File"
	print "\t[2] To Decrypt The File"
	user_choose = raw_input("Enter Number of Your Choose Here: ")
	file_name = raw_input("Enter Name File: ")
	if user_choose != "" and file_name != "" and file_name in list_files:
		if int(user_choose) == 1:
			print "Enter the encryption key number and it must be positive and be greater than or equal to 1 or less than or equal to 25".capitalize()
			key = int(raw_input("Enter Key: "))
			if file_name[-4:] == ".txt":
				old_file = open(file_name,"r")
				old_file_read = old_file.readlines()
				old_file.close()
				os.remove(file_name)
				new_file_content = ""
				for sen in old_file_read:
					new_file_content += EncryptTheSentence(sen, key)
				print "All DONE!"
				print "=" * 25
				print new_file_content
			else:
				print "Sorry :( The File Extension Is Incorrect"
			new_file = open(EncryptTheSentence(file_name[:-4], key) + ".txt","w+")
			new_file.write(new_file_content)
		elif int(user_choose) == 2:
			print "Enter the decryption key number and it must be positive and be greater than or equal to 1 or less than or equal to 25".capitalize()
			key = int(raw_input("Enter Key: "))
			if file_name[-4:] == ".txt":
				old_file = open(file_name,"r")
				old_file_read = old_file.readlines()
				old_file.close()
				os.remove(file_name)
				new_file_content = ""
				for sen in old_file_read:
					new_file_content += DecryptTheSentence(sen, key)
				print "All DONE!"
				print "=" * 25
				print new_file_content
			else:
				print "Sorry :( The File Extension Is Incorrect"
			new_file = open(DecryptTheSentence(file_name[:-4], key) + ".txt","w+")
			new_file.write(new_file_content)
		else:
			print "Error Choose"
		status = "OK"
	else:
		status = "Error"
		print "Error Try Again"
new_file.close()
