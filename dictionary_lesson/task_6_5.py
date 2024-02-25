rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Dnipro": "Ukraine"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("List of rivers:")
for river in rivers:
    print(river)

print("List of countries:")
for country in rivers.values():
    print(country)
