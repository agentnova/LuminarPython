from re import *
# pattern="[abc]" #check either a or b or c
# pattern="[a-z]" #check a to z lowercase
# pattern="[A-Z]" #check A to Z uppercase
# pattern="[a-zA-Z]" #check both uppercase and lowercae
# pattern="[0-9]" #check digits
# pattern="[^0-9]" #except 0-9
# pattern="[^a-zA-Z0-9]" #except all these(check for special characters

# predefined characters
# pattern="\s" #space
# pattern="\d" #digit
# pattern="\D" #except digit
# pattern="\w" #check for all words
pattern="\W" #special characters
matcher=finditer(pattern,"abx 7Zxy@")
for match in matcher:
    print(match.start())
    print(match.group())