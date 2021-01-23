#word_present_in_text.py
#eyecode4you.wordpress.com/

""" Here we will check to see if the characters of one string is 
	contained within another string.
	Without using Regular Expressions (re or regex modules).
"""

word = input("Enter Word to Search for: ")
str_to_check = input("Enter text to check: ")
display_str = str_to_check

'''Ensure both strings are the same format for comparison.
   Remember strings are case sensitive, A and a aren't the same!
'''
word = word.lower()
str_to_check = str_to_check.lower()

#Variable to count characters common in both Strings
cnt = 0

'''For each character in word, check against chars in str_to_check and 
   if present increment cnt '''
for char in word:
	if char in str_to_check:
		cnt += 1
        
		""" Here when a match is found we will create a new string, 
		removing the matched character to prevent matching multiple 
		characters in word to a single character in str_to_check """
		x = str_to_check.index(char)
		#Slice string in two, removing matched char, then rejoin
		str_to_check = str_to_check[0:x] + str_to_check[x+1:]
		print("\n--->", str_to_check)
		print("Character Removed:", char)
      
#Display data
print("\nLength of word:", len(word))
print("Length of Counter variable:", cnt)

#If cnt and length of word is equal print match
if cnt == len(word):
    print("\n-->Found:", word, "in", display_str)
else:
    print("\n-->", word, "not found in:", display_str)
