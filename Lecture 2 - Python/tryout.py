x = input()
dic = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
       "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
for i in x:
    print(dic.get(i, "Not a number"), end="-")

print()
