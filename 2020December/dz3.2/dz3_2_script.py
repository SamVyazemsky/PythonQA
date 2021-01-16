import json
from csv import DictReader

with open("../dz3.2/users.json", "r") as fu:
    users = json.loads(fu.read())

with open('../dz3.2/books.csv', newline='') as fb:
    reader = DictReader(fb)
    books = []
    for row in reader:
        books.append(row)

new_list = []
if len(users) == 0 or len(books) == 0:
    print('no elements to write')
else:
    for i in range(0, min(len(users), len(books))):
        new_list.append({
            "name": users[i]['name'],
            "gender": users[i]['gender'],
            "address": users[i]['address'],
            "books": [{
                "title": books[i]['Title'],
                "author": books[i]['Author'],
                "height": books[i]['Height']
            }]
        })

    if len(books) < len(users):
        for i in range(len(books), len(users)):
            new_list.append({
                "name": users[i]['name'],
                "gender": users[i]['gender'],
                "address": users[i]['address'],
                "books": []
            })

with open("users_with_books.json", "w") as f:
    new_list_json = json.dumps(new_list, indent=7)
    f.write(new_list_json)

