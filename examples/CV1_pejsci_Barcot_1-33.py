n = int(input("Zadejte počet pejsků: " ))
for i in range(n, 0, -1):
    if i == 1:
        print(f"{i} pejsek jde na výlet sám.")
    elif i in [2, 3, 4]:
        print(f"{i} pejsci jdou na výlet, jeden se zaběhl.")
    else:
        print(f"{i} pejsků jde na výlet a jeden se zaběhl.")
