#Accept any city from the user and display monument of that city.
                  # City                                 Monument
                  # Delhi                               Red Fort
                  # Agra                                Taj Mahal
                  # Jaipur                              Jal Mahal

city=input("enter city")

if(city=='delhi'):
    print("monument is red fort")
elif(city=='agra'):
    print("monument is taj mahal")
elif(city=='jaipur'):
    print("monument is jal mahal")
else:
    print("invalid")

