import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat 
bat 
mat pat
'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\D')
#pattern = re.compile(r'\d{2}')
#pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
#pattern = re.compile(r'[0-9a-zA-Z]')
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'[^a-zA-Z0-9]')
#pattern = re.compile(r'[^b]at')
pattern = re.compile(r'(Mr|Ms|Mrs)')




matches = pattern.finditer(text_to_search)
for select in matches:
    print(select)

print(matches)
