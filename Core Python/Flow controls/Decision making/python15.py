#print your age

cur_year=int(input("enter the current year"))
cur_month=int(input("enter the current month"))
cur_date=int(input("enter the current date"))
bir_year=int(input("enter the birth year"))
bir_month=int(input("enter the birth month"))
bir_date=int(input("enter the birth date"))
age=0
if(cur_year>bir_year):
    if(cur_month>bir_month):
        if(cur_date>bir_date):
           print("age=",cur_year-bir_year)

else:
    print("invalid")



