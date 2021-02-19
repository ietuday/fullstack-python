# https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/
# https://www.learnpython.org/en/Loops

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
     if item == 'spam':
         break

print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages", "spam"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it")


from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days=1) # today + 1 day is tomorrow
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8 # equivalent to applying 20% discount
    print(
        'Price for sku', product['sku'],
        'is now', product['price'])


items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate to True
found = False # this is called "flag"
for item in items:
    print('scanning item', item)
    if item:
        found = True # we update the flag
        break
if found: # we inspect the flag
    print('At least one item evaluates to True')
else:
    print('All items evaluate to False')