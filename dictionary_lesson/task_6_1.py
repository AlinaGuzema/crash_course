people = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 30,
    "city": "Boston",
}
# print("First name :", people["first_name"])
# print("Last name :", people["last_name"])
# print("Age:", people["age"])
# print("City:", people["city"])

# Як можна було зробити
for key, value in people.items():
    print(key, ":", value)
