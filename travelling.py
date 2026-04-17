travel_data =(
    ("Paris",("Eiffel Tower" , "Croissant", "Spring")),
    ("Tokyo",("Shibuya Crossing" , "sushi ", "Spring")),
    ("New York", ("Statue of Liberty", "Pizza","fall")),
    ("Dubai", ("Burj Khalfi", "Shawarma", "Winter"))
            )

print("Choose a city to explore: \n")

for i in range(len(travel_data)):
    print(i+1, ".", travel_data[i][0])

choice = int(input("\nEnter your choice number: "))
index = choice - 1 
selected_city = travel_data[index]
print("\nTravel details: ")
print("city:" , selected_city[0])
print("Must vist:" , selected_city[1][0])
print("Try food:" , selected_city[1][1])
print("Best season:" , selected_city[1][2])