import json
from csv import DictReader

with open("DZ_scriptfiles/users.json", "r") as fileusers:
    users = json.loads(fileusers.read())

with open("DZ_scriptfiles/books.csv", newline='') as filebooks:
    reader = DictReader(filebooks)
    books = []
    for row in reader:
        books.append(row)

new_list = []
if len(users) == 0 or len(books) == 0:
    print('There is no elements to write')
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
