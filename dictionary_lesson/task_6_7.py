person_one = {"name": "Alina", "last_name": "Guzema"}
person_two = {"name": "John", "last_name": "Smith"}
person_three = {"name": "Anna", "last_name": "Bont"}
people = [person_one, person_two, person_three]
for i, person in enumerate(people):
    print(f"Person {i}:")
    for k, v in person.items():
        print(f"\t{k}: {v}")
