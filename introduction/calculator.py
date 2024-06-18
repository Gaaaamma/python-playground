file: str = "./money.csv"

sum: int = 0

cost = {
    "Dad": 0,
    "Mom": 0,
    "grandma": 0,
    "peter": 0,
}

with open(file) as file:
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        day, people, item, money = line
        sum += int(money)
        if item == "娛樂費":
            cost[people] += int(money)
        print(day, people, item, money)
print(sum)
print(cost)