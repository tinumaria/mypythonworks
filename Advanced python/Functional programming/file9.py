#1. Find all of the numbers from 1-1000 that are divisible by 7
#2. Find all of the numbers from 1-1000 that have a 3 in them
#3. Count the number of spaces in a string.
#4. Create a list of all the consonants in the string
#   “Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams”

#1.
lst=[i for i in range(1,1001) if i%7==0]
print(lst)

#2.
lst=[i for i in range(1,1001) if '3' in str(i)]
print(lst)

#3.
line='Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams'
lst=[i for i in line if i==' ']
print(len(lst))

#4.
vowels='aeiou'
lst=[i for i in line if i not in vowels]
print(lst)

