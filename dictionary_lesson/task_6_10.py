favorite_numbers = {
    "Alina": [1, 4, 7],
    "Bob": [5, 8, 9],
    "John": [5.9]
}
for person, numbers in favorite_numbers.items():
    print(f"{person}’s favorite number : ")
    for number in numbers:
        print(f"\t- {number}")
