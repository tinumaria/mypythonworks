#merge lst & dic

#fromkeys method - it return a dictionary with specified keys & specified values

employee=['tinu','siva']
default={'desig':'python','sal':10000}

res=dict.fromkeys(employee,default)
print(res)

print(res['tinu'])





