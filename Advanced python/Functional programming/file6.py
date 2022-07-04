#print y if vowels else print n using list comprehension

name='luminartechnolab'
vowels='aeiou'
lst=["y" if i in vowels else "n" for i in name]
print(lst)