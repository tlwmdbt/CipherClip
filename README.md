# cipherclip
By Daniel Toschläger, 2020

Description: A Cipher Generator for PC's. It generates a 16 character alpha-numeric cipher with special characters and writes it directly into the Windows clipboard to be pasted from there. If available /dev/urandom or it's actual equivalent in the OS is used to seed the python random functions. If urandom is not available the standard randint() function is used.

Conventions:
The password will have 16 characters. The first letter is from the latin alphabet, lower or upper case. All other digits can also contain numbers and special characters. No duplicate digits.

Dependencies:
1. Clipboard https://pypi.org/project/clipboard/ by Terry Yin https://pypi.org/user/Terry.Yin/
2. An interpreter (>3.8) capable of loading the OS module and optional interfacing /dev/urandom or it's OS equivalent

Disclaimer:
No guarantee is provided for randomness or security for the end system or user. This script is not eligible for a production enviroment. Use at your own risk.
