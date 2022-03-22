# Filename: citc1301a02-creed23-lab08.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab08
# Due Date: Feb 11 2020
# Description: String Methods



def main():
   str1= '     Spam, spam, spaM, sPaM     '
   print(f' {len(str1)}')
   # This command tells you how many characters are used in the varaible that we printed
   print(f' {str1.upper()}')
   # This command puts all the letter characters is all caps that is contained within the variable
   print(f' {str1.lower()}')
   # This command puts all the letter characters in lower case that is contained within the variable
   print(f' {str1.title()}')
   # This command will capitalize the first letter in each word within our variable
   print(f' {str1.strip()}')
   # This command strips all of the extra spaces at the begining and end of our statement within our variable
   print(f' {str1.lstrip()}')
   # This command strips all of spaces at the begining(left) side of the statement within our varaible
   print(f' {str1.rstrip()}')
   # This command strips all of the spaces at the end(right) side of the statement within our variable


   print(str1.title().lower())
   print(str1.lower().title())
   # These two commands differ because of the .statment. The .lower() will make everything lowercase while the .title()
   # will make the first letter in each word uppercase.





main()