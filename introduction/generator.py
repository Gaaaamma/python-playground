from typing import List, Tuple
from random import randint

MONTH: int = 7
DAY: Tuple[int, int] = (1, 31)
MIN_COST: int = 10
MAX_COST: int = 1000

family_list: List[str] = ["Dad", "Mom", "grandma", "peter"]
item_list: List[str] = ["早餐", "午餐", "晚餐", "日用品", "娛樂費"]

def generate_csv():
    for day in range(DAY[0], DAY[1]+1):
        record: int = randint(0, 10)
        for _ in range(record):
            people: int = randint(0, len(family_list)-1)
            item: int = randint(0, len(item_list)-1)
            print(f"{MONTH}/{day},{family_list[people]},{item_list[item]},{randint(MIN_COST, MAX_COST)}")

generate_csv()