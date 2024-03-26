import re

regexp = 'python'
string = 'pyton'
# regexp = 'pyth'
# string = 'python'
# regexp = 'thon'
# string = 'python'
# regexp = 'PYTHON'
# string = 'python'
print("Template -> ", regexp)
res = re.match(regexp, string)
print(res)

regexp = 'python .'
print("Template -> ", regexp)
print(re.match(regexp, 'python 2'))
print(re.match(regexp, 'python 3'))
print(re.match(regexp, 'python !'))
print(re.match(regexp, '--- python 3.11'))

regexp = 'pytho?'
print("Template -> ", regexp)
print(re.match(regexp, 'pytho'))
print(re.match(regexp, 'python'))
print(re.match(regexp, 'pytho3'))
print(re.match(regexp, ' python3'))

regexp = 'regexp?'
print("Template -> ", regexp)
print(re.match(regexp, 'regex'))
print(re.match(regexp, 'regexp'))
print(re.match(regexp, 'regexx'))

regexp = 'regexp\\?'
print("Template -> ", regexp)
print(re.match(regexp, 'regex'))
print(re.match(regexp, 'regexp'))
print(re.match(regexp, 'regexp?'))

print(re.match('\\\\', '\\'))

regexp = '[bd]a[td]'
print("Template -> ", regexp)
print(re.match(regexp, 'bat'))
print(re.match(regexp, 'dad'))
print(re.match(regexp, 'cat'))
print(re.match(regexp, 'bot'))

regexp = 'Python [?.]'
print("Template -> ", regexp)
print(re.match(regexp, 'Python ?'))
print(re.match(regexp, 'Python .'))
print(re.match(regexp, 'Python !'))

regexp = 'ja[a-z]'
print("Template -> ", regexp)
print(re.match(regexp, 'jazz'))
print(re.match(regexp, 'jam'))
print(re.match(regexp, 'jaZ'))
print(re.match(regexp, 'ja1'))

regexp = '[A-Z]ill'
print("Template -> ", regexp)
print(re.match(regexp, 'Bill'))
print(re.match(regexp, 'bill'))
print(re.match(regexp, '1ill'))

regexp = '[2-9a-c!?A-Q]'
print("Template -> ", regexp)
print(re.match(regexp, 'Z'))
print(re.match(regexp, 'n'))
print(re.match(regexp, '1'))
print(re.match(regexp, '?'))
print(re.match(regexp, ','))

regexp = '[^A-C]'
print("Template -> ", regexp)
print(re.match(regexp, 'Bond'))
print(re.match(regexp, 'Fond'))

regexp = '[A-C^]'
print("Template -> ", regexp)
print(re.match(regexp, 'Bond'))
print(re.match(regexp, 'Fond'))
print(re.match(regexp, '^ond'))

regexp = '[\\w!?]'
# regexp = '[\\d!?]'
# regexp = '[\\W!?]'
# regexp = '[\\D!?]'
print("Template -> ", regexp)
print(re.match(regexp, 'Z'))
print(re.match(regexp, 'n'))
print(re.match(regexp, '1'))
print(re.match(regexp, '?'))
print(re.match(regexp, ','))
print(re.match(regexp, '_'))

regexp = "wo+w!"
print("Template -> ", regexp)
print(re.match(regexp, 'wow!'))
print(re.match(regexp, 'woooooooow!'))
print(re.match(regexp, 'ww!'))

regexp = "Python [1-9]+"
print("Template -> ", regexp)
print(re.match(regexp, 'Python 111111'))
print(re.match(regexp, 'Python 122345'))
