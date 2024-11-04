user = {"first_name": "Mary-Beth",
        "middle_name": "Gabriella",
        "last_name": "Agulhas",
        "age": 24,
        "date_of_birth": "05.11.2000"}

# Complexity: O(1)
user["date_of_birth"] = "06.20.1971"
user["date_of_birth"] = "03.15.1965"
print(user["date_of_birth"])

# .pop and del performs the same delete method in the dictionaries at different speeds
# Complexity: O(1)
user.pop("date_of_birth")
#del user["date_of_birth"]

print(user)

print(user.keys())
print(user.values())
print(user.items())