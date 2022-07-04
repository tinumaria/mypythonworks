#basic rules

import re
count=0
rule='[abcs]'

matcher=re.finditer(rule,'abc @siva123')

#how much times abcs matches will be printed

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)

#if we give rule='[^abcs]'
# ^ shows except abcs others will be printed

#if we give rule='[a-z]'
# shows from a to z, matching will be printed

#if we give rule='[0-9a-zA-Z]'
# shows from 0-9,a-z,A-Z matching will be printed