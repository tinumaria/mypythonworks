results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90, "A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win": 95, "A+": 50000},
    {"district":"mpm","win": 90, "A+": 4500},
]

#1. win % of tvm
# for i in results:
#     if i["district"]=="tvm":
#         print(i["win"])
#we should do in short (list comprehension)
tvm_win=[i["win"] for i in results if i["district"]=="tvm"]
print(tvm_win)

#2. district with highest win %
high=max(results,key=lambda i:i["win"])
print(high["district"])

#3. district with lowest win %
low=min(results,key=lambda i:i["win"])
print(low["district"])

#4. district with highest A+
high1=max(results,key=lambda i:i["A+"])
print(high1["district"])

#5. district with lowest A+
low1=min(results,key=lambda i:i["A+"])
print(low1["district"])

#6. total number of A+
total=sum(i["A+"] for i in results)  #key=lambda wont work in sum
print(total)

#7. total win 
total1=sum(i["win"] for i in results)
print(total1)

#8. sort district wrt win % in ascending order
results.sort(key=lambda i:i["win"]) #lambda syntax
print(results)

#9. sort district wrt win % in discending order
results.sort(key=lambda i:i["win"],reverse=True)
print(results)