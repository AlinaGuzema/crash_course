pet_one = {"kind": "cat", "owner": "Alina"}
pet_two = {"kind": "dog", "owner": "John"}
pet_three = {"kind": "bird", "owner": "Bob"}

pets = [pet_one, pet_two, pet_three]

for pet in pets:
    for k, v in pet.items():
        print(f"Pet {k}: {v}")
    # print(f"Pet kind: {pet['kind']}")
    # print(f"Pet owner:{pet['owner']}")
