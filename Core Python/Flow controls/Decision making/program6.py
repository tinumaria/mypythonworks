#company decided to give a bonus of 5% to employee if his/her year of service is more than 5 years
# Ask user for their salary and year of service and print net bonus amount

sal=int(input("enter salary"))
year=int(input("enter year of service"))
bonus=sal*0.05

if(year>5):
  print("net bonus amount is",bonus)
else:
  print("you are not eligible")

#or

sal = int(input("enter salary"))
year = int(input("enter year of service"))

if(year>5):
  print("net bonus amount is", sal*0.05)
else:
  print("you are not eligible")