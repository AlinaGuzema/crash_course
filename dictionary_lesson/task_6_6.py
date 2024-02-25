favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
people_to_poll = ["alina", "john", "charlie", "dina", "frank", "grace"]

for person in people_to_poll:
    if person.lower() in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"Hi {person.title()}, we invite you to take the favorite languages poll!")
