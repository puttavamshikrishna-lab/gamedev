cart = ("Samhita" , ["Milk", "Chocolate", "Candies", "Chips"])

print("Intial Cart: \n" , cart)


cart[1].append("Apples")
print("\nAfter adding Apples: \n" , cart)

cart[1].remove("Milk")
print("\nAfter removing milk: \n" , cart)

cart[1][3] = "soft drink"
print("\nAfter replacing Apple:\n", cart)

print("Owner:" , cart[0])
print("Items:" , cart[1])