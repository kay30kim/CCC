n = int(input())
pepper_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

total_spiciness = 0
for i in range(n):
    pepper_name = input()
    total_spiciness += pepper_dict[pepper_name]

print(total_spiciness)