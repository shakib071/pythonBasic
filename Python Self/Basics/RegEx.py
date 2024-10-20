# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern

#Python has a built-in package called re, which can be used to work with Regular Expressions

import re 

txt="The rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x) #The ar Spain txt te acea kina seta dekhbe



txt="The rain in Spain"
x = re.search("^Th.*Spain$",txt) #full same na holeoo cholbe 
print(x)
#pattern khujbe shudhu

#method gula notion a acea


#The findall() function returns a list containing all matches.

txt = "The rain in Spain"
x=re.findall("ai",txt)
print(x) 

# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned


# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned

#Search for the first white-space character in the string
txt = "The rain in Spain"
x=re.search("\s",txt)

print("The first white-space character is located in position:",x.start())
#1st white space carecter er location num debe

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) #no match return none



#The split() function returns a list where the string has been split at each match

txt = "The rain in Spain"
x= re.split("\s",txt) #\s diye white space khuje 
#white space a split korbe
print(x)
#You can control the number of occurrences by specifying the maxsplit parameter


txt = "The rain in Spain"
x = re.split("\s", txt, 1) #1st occurance of whitespace a split korbe
print(x)


# The sub() function replaces the matches with the text of your choice

txt = "The rain in Spain"
x = re.sub("\s", "9", txt) #The sub() function replaces the matches with the text of your choice
print(x)


#You can control the number of replacements by specifying the count parameter

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match





