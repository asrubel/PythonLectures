import re

regexp = "go*d!"
print("Template -> ", regexp)
print(re.match(regexp, 'god!'))
print(re.match(regexp, 'goooooood!'))
print(re.match(regexp, 'gd!'))
print(re.match(regexp, 'gid!'))

regexp = ".*no.*"
print("Template -> ", regexp)
print(re.match(regexp, 'no'))
print(re.match(regexp, 'no!!!!! please no!!!! no!!!'))
print(re.match(regexp, 'I have no experience in regexp'))

regexp = "\\w{5}"
print("Template -> ", regexp)
print(re.match(regexp, 'no'))
print(re.match(regexp, 'noooo'))
print(re.match(regexp, 'noo oooooo'))

regexp = "\\d{5,10}"
print("Template -> ", regexp)
print(re.match(regexp, '1234'))
print(re.match(regexp, '12345'))
print(re.match(regexp, '1234567'))
print(re.match(regexp, '1234567890'))
print(re.match(regexp, '12345678901234 wwww'))

regexp = "\\d{,4}"
print("Template -> ", regexp)
print(re.match(regexp, '123'))
print(re.match(regexp, '12345'))
print(re.match(regexp, '12'))
print(re.match(regexp, '1'))
print(re.match(regexp, 'sdfsdgsdg'))

regexp = "(h[ao]){2}"
print("Template -> ", regexp)
print(re.match(regexp, 'ha'))
print(re.match(regexp, 'haha'))
print(re.match(regexp, 'ho'))
print(re.match(regexp, 'hoho'))
print(re.match(regexp, 'haho'))
print(re.match(regexp, 'hoh'))
print(re.match(regexp, 'hooooho'))
print(re.match(regexp, 'ahaha'))

regexp = "(python|kotlin|java|C#)"
print("Template -> ", regexp)
print(re.match(regexp, 'python'))
print(re.match(regexp, '-javascript'))
print(re.match(regexp, 'rust'))
print(re.match(regexp, 'dart'))
print(re.match(regexp, 'java'))
print(re.match(regexp, 'C++'))
print(re.match(regexp, 'C#'))

regexp = "(python|kotlin|java|C#) (lecture|practice|exam)"
print("Template -> ", regexp)
print(re.match(regexp, 'python lecture'))
print(re.match(regexp, 'javascript exam'))
print(re.match(regexp, 'rust workshop'))
print(re.match(regexp, 'dart session'))
print(re.match(regexp, 'java exam'))
print(re.match(regexp, 'C++ assignment'))
print(re.match(regexp, 'C# practice'))

regexp = "(\\+38|^)0(66|67|68|95|96|97|98|99)\\d{7}"
print("Template -> ", regexp)
print(re.match(regexp, '+380986667788'))
print(re.match(regexp, '+380986667786668'))
print(re.match(regexp, '+3803366677866'))
print(re.match(regexp, '3803366677866'))
print(re.match(regexp, '09866677866'))
