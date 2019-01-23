#this is a note from Philip

#program should ask for name,
#ask if message should be encrypted or decrypted
#ask for plaintext or ciphertext
#ask for key 


#predefined variables
mode= ''
options=['E','D']
MAX_NAME_SIZE=12
keyLists= ['1','2','3','4','5','6','7',
'8','9','10','11','12','13','14','15',
'16','17','18','19','20','21','22','23','24','25','26']


#the letters that can be encrypted
LETTERS = "abcdefghijklmnopqrstuvwxyz"




#validate name input
def checkName(n):
	if str(n).isalpha()== True:
		if len(n)>=3: #ensures at least 3 letters are entered for name
			return n
		else:
			return False
	else:
		return False
			


uName= input("Hello, what's your name? (3-12 chars): ").capitalize()

while checkName(uName)== False:
	uName= input("Please enter your name properly (3-12 chars): ").capitalize()
else:
	uName= uName[:MAX_NAME_SIZE] #truncates name input to 12 letters
	print("Glad to have you, "+ str(uName)+"! ")
	

cryptType=input("Would you like to Encrypt or Decrypt? (choose E or D): ").upper()
while cryptType not in options:
	cryptType=input('Error. Enter E for Encrypt or D for Decrypt: ').upper()

if cryptType=='E': #run encryption
	mode='Encrypt'
	print ("You have chosen to encrypt your message.")
else:
	mode='Decrypt'
	print("You have chosen to decrypt your message.")

keyNum=input("Please choose a key (1 - 26): ")
while keyNum not in keyLists:
	keyNum= input("Try again. Key must be a number 1 - 26: ")
else:
	print ("You have chosen " + str(keyNum) + " as your key.")

if cryptType=='E': #run encryption
	mode='Encrypt'
	mode= input('Enter your message in plaintext: ')
	for LETTERS in mode:
		x= ord(LETTERS)
		x= (int(x) + int(keyNum))
		print ((chr(x)), end="" )
else:
	mode='Decrypt'
	mode= input('Enter your message in ciphertext: ')
	for LETTERS in mode:
		x= ord(LETTERS)
		x=(int(x) - int(keyNum))
		print ((chr(x)), end="")
		#else: #run decryption
    	#mode= 'Decrypt'
	#mode= input('Enter your message: )


