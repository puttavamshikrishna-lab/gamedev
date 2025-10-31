countries={"USA":"D.C", "India":"New Delhi", "Brazil":"Brasilia"}
print(countries["USA"])
countries["UK"]="London"
print(countries.keys())
print(countries.values())
print(countries["UK"])
print(len(countries))
print("USA"in countries)
print("Srilanka"in countries)
del countries["India"]
print(countries.keys())
countries["USA"]="Washingtion DC"

countries={"Austrila":"Canberra", "France":"Paris", "Italy":"Rome",}
print(countries.keys())
print(countries.values())
countries["UK"]="London"
print(countries.keys())
print(countries.values())