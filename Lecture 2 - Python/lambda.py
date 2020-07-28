people = [
    {"Name": "Jason", "Note": "17"},
    {"Name": "Hermione", "Note": "12"},
    {"Name": "Shawn", "Note": "11"}
]


def f(person):
    return person["Name"]


people.sort(key=f)
print(people)
