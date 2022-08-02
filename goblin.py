# A simple wordlist generator 


from concurrent.futures.process import _python_exit
import itertools


ban = '''

                                                    '''

print('██╗    ██╗ ██████╗ ███████╗███╗   ██╗')
print('██║    ██║██╔════╝ ██╔════╝████╗  ██║')
print('██║ █╗ ██║██║  ███╗█████╗  ██╔██╗ ██║')
print('██║███╗██║██║   ██║██╔══╝  ██║╚██╗██║')
print('╚███╔███╔╝╚██████╔╝███████╗██║ ╚████║')
print(' ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝')
print('')
print('______________________________________')
print('')
print('Developed by RICK @HacklikeHacker') 
print('v: 1.0')
print('')
print('______________________________________')
print('')

# Metion the string length in ratio format.

scale = input('\033[36m[!] provide a size scale [eg: "1 to 50" = 1:5] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

#Customize the string length without the leading spaces	

use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [Y/N]: "))
if use_nouse == 'Y':
	first_name = str(input("\n\033[36m[*] Fist Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birthday: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	father_name = str(input("\n\033[36m[*] FatherName: "))	
	Mother_name = str(input("\n\033[36m[*] MotherName: "))
	Partner_name = str(input("\n\033[36m[*] PartnerName: "))
	Girlfriend_name = str(input("\n\033[36m[*] GirlfriendName: "))	
	Friends_name = str(input("\n\033[36m[*] FriendsName: "))	
	Religion_name = str(input("\n\033[36m[*] ReligionName: "))	
	Pet_name = str(input("\n\033[36m[*] PetName: "))	
	phone_number = str(input("\n\033[36m[*] PhoneNumber: "))
	Favourite_colour = str(input("\n\033[36m[*] FavouriteColour: "))
	Children_name = str(input("\n\033[36m[*] ChildrenName: "))	
	Grand_children_name = str(input("\n\033[36m[*] GrandChildrenName: "))	
	Email_Id = str(input("\n\033[36m[*] EmailId: "))	


# You can customize the string format

	chrs = first_name + last_name + birthday + month + year + father_name + Mother_name	+ Partner_name + Girlfriend_name	+ Friends_name + Religion_name + Pet_name + phone_number + Favourite_colour + Children_name + Grand_children_name + Email_Id
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\'{}^ '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Give a name for your wordlist: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
