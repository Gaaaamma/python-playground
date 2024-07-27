from typing import Dict

file: str = "./money.csv"

sum: int = 0

cost: Dict[str, int] = {
    "Dad": 0,
    "Mom": 0,
    "grandma": 0,
    "peter": 0,
}

entertainment: Dict[str, int] = {
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
        cost[people] += int(money)
        if item == "娛樂費":
            entertainment[people] += int(money)
        print(day, people, item, money)
print("\n=======================")
print(f"這個月全家共花費: {sum}")
print(f"這個月每人各花費: {cost}")
print(f"這個月每人娛樂費花費: {entertainment}")
print("=======================")