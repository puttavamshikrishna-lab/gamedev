address = ("272","Brickfield shelters", "Banglore", "Karnataka" , "873029")
for x in address:
    print(x,end= " ")

#UNPACKING
houseno, apartment , city, state , pincode= address 
print("\nHouse No. :", houseno)
print("Apartment Name: " , apartment)
print("City:", city)
print("State:", state)
print("Pincode:" , pincode)

my_tuple= 3,4.6, "dog"
print(my_tuple)

#Nested tuple
#lists , tuples

nestedtuple= ("mouse", [8,5,4], (1,2,3))
print(nestedtuple[0][3])
print(nestedtuple[1][1])

