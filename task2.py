import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if(min < 1 or max > 1000 or max - min < quantity - 1):
        return list()
    else: 
        result_set = set()
        while(len(result_set) < quantity):
            result_set.add(random.randint(min, max))
        result_list = list(result_set)
        result_list.sort()
        return result_list

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 6, 6))
print(get_numbers_ticket(6, 1, 6))
print(get_numbers_ticket(1, 10, 10))
print(get_numbers_ticket(100, 1001, 10))
print(get_numbers_ticket(100, 110, 10))
print(get_numbers_ticket(1, 1000, 100))
print(get_numbers_ticket(-1, 10, 1))
print(get_numbers_ticket(1, 4, 5))
print(get_numbers_ticket(1, 1, 1))
