# Strings are immutable objects in Python

string = "I love sweet roll chupa chups gingerbread chocolate soufflé lollipop."

# string concatenation (+)
first_str = "Hello"
second_str = "World"
result = first_str + second_str
print(result)

# len() Returns the length of an object (counting start from 1)
name = "jane bone"
len_of_name = len(name)
print(len_of_name)

# String Methods

# capitalize()	        Converts the first character to upper case
cap_str = name.capitalize()
print(cap_str)
print(type(cap_str)) # <class 'str'>

# casefold()	        Converts string into lower case
str1 = "ENGLAND"
str_case = str1.casefold()
print(str_case)
print(type(str_case)) #<class 'str'>

# center()	            Returns a centered string
center = str1.center(20,"-")
print(center)
print(len(center)) # 20
print(type(center)) # <class 'str'>

# count()	            Returns the number of times a specified value occurs in a string
sample = "The quick brown fox jump over the lazy dog"
count = sample.count("The")
print(count)
print(type(count)) # <class 'int'>

# encode(encoding="",errors="")	            Returns an encoded version of the string
# encodings
# UTF-8
# ASCII
# ISO-8859-1 (Latin-1)
# UTF-16
# UTF-32
# CP1252 (Windows-1252)
# Big5
# Shift_JIS

# errors
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	            - ignores the characters that cannot be encoded
# 'namereplace'	        - replaces the character with a text explaining the character
# 'strict'	            - Default, raises an error on failure
# 'replace'	            - replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character

firstname = "အောင်Aung"
encode = firstname.encode(encoding="ASCII",errors="namereplace")
print(encode)
print(type(encode)) # <class 'bytes'>

# endswith()	        Returns true if the string ends with the specified value
find_end = sample.endswith("dog")
print(find_end)
print(type(find_end)) # <class 'bool'>

# expandtabs()	        Sets the tab size of the string
st1 = "-Content\n"
st2 = "\t-sub content 1\n"
st3 = "\t-sub content 2\n"
st4 = "\t-sub content 3\n"
fst = st1+st2+st3+st4
tabs = fst.expandtabs(3)
print(tabs)

# find()	            Searches the string for a specified value and returns the position of where it was found
family = "We love our family"
find = family.find("A", 0,len(family))
print(find) # -1
print(type(find)) # <class 'int'>

# format()	            Formats specified values in a string

# format_map()	        Formats specified values in a string
# index()	            Searches the string for a specified value and returns the position of where it was found
# isalnum()	            Returns True if all characters in the string are alphanumeric
# isalpha()	            Returns True if all characters in the string are in the alphabet
# isascii()             Returns True if all characters in the string are ascii characters
# isdecimal()	        Returns True if all characters in the string are decimals
# isdigit()	            Returns True if all characters in the string are digits
# isidentifier()	    Returns True if the string is an identifier

# islower()	            Returns True if all characters in the string are lower case
islower = sample.islower()
print(islower)
print(type(islower)) #<class 'bool'>

# isnumeric()	        Returns True if all characters in the string are numeric
# isprintable()	        Returns True if all characters in the string are printable
# isspace()	            Returns True if all characters in the string are whitespaces
# istitle()	            Returns True if the string follows the rules of a title

# isupper()	            Returns True if all characters in the string are upper case
isupper = str1.isupper()
print(isupper)
print(type(isupper))

# join()	            Converts the elements of an iterable into a string
# ljust()	            Returns a left justified version of the string
# lower()	            Converts a string into lower case
lower = str1.lower()
print(lower)
print(type(lower)) #<class 'str'>

# lstrip()	            Returns a left trim version of the string
# maketrans()	        Returns a translation table to be used in translations
# partition()	        Returns a tuple where the string is parted into three parts
# replace()	            Returns a string where a specified value is replaced with a specified value
# rfind()	            Searches the string for a specified value and returns the last position of where it was found
# rindex()	            Searches the string for a specified value and returns the last position of where it was found
# rjust()	            Returns a right justified version of the string
# rpartition()	        Returns a tuple where the string is parted into three parts
# rsplit()	            Splits the string at the specified separator, and returns a list
# rstrip()	            Returns a right trim version of the string
# split()	            Splits the string at the specified separator, and returns a list
# splitlines()	        Splits the string at line breaks and returns a list

# startswith()	        Returns true if the string starts with the specified value
findstart = sample.startswith("The")
print(findstart)
print(type(findstart)) # <class 'bool'>

# strip()	            Returns a trimmed version of the string
# swapcase()	        Swaps cases, lower case becomes upper case and vice versa

# title()	            Converts the first character of each word to upper case
tit_str = name.title()
print(tit_str)
print(type(tit_str)) # <class 'str'>

# translate()	        Returns a translated string

# upper()	            Converts a string into upper case
upper = sample.upper()
print(upper)
print(type(upper)) # <class 'str'>

# zfill()	            Fills the string with a specified number of 0 values at the beginning
