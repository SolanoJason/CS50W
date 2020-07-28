people = [
{"Name":"Jason","Note":"17"},
{"Name":"Hermione","Note":"12"},
{"Name":"Shawn","Note":"11"}
]

people.sort(key=lambda person: person["Name"])
print(people)
