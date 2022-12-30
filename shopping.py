shopping_list = [{"item": "milk", "price": 2.99},
                 {"item": "pasta", "price": 1.99},
                 {"item": "eggs", "price": 3.99},
                 {"item": "spam", "price": 2.99},
                 {"item": "bread", "price": 2.99},
                 {"item": "rice", "price": 3.99}]
budget = 10.0

for item in shopping_list:
    if budget - item["price"] <= 0:
        print("Oops, out of money! You have {:.3} leftover".format(budget))
        break
    budget -= item["price"]

    print("Buy " + item["item"])


s_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for index in range(len(s_list)):
    if s_list[index] == item_to_find:
        found_at = index
        break

print(item_to_find + " found at " + str(found_at))