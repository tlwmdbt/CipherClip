# Password Generator
#================================
from random import choice, seed, randint
from os import urandom
import clipboard
#================================
seed(int.from_bytes(urandom(100), byteorder='big', signed=False))

# nescessary temporary list and a counter
tmp_passwd = []
PwdLength = 16
counter = 1

# while loop to create and choose from a alpha numeric and special character set
while counter <= PwdLength:
  # setup the set of characters to choose from randomly, first character is a letter
  if counter == 1:
    element = choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  else:
    element = choice('ÖÄÜöäüABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^*()-_=+[]|;:,.<>/?.')
  # no duplicates of elements
  if element not in tmp_passwd:
    # append it to the temporary list tmp_passwd
    tmp_passwd.append(element)
    # count +1
    counter = counter + 1


# construct the password from entrys of the temporary list and copy it to Win-clipboard
password = "".join(tmp_passwd)  
clipboard.copy(password)
#text = clipboard.paste()  # text will have the content of clipboard

# bye
raise SystemExit
