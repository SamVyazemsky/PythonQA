import json
import csv


class DataCombiner:
    """Класс совмещающий датасет пользователей в формате json с датасетом книг в формате csv"""

    def __init__(self, path_users: str, path_to_books: str):
        self.path_users = path_users
        self.path_to_books = path_to_books
        self.users = self._open_json()
        self.books = self._open_csv()
        self.data_combination = self._combine_data()

    def _open_json(self):
        with open(self.path_users, 'r') as json_file:
            return json.loads(json_file.read())

    def _open_csv(self):
        with open(self.path_to_books, 'r') as csv_file:
            raw_data = csv_file.read()
            data = csv.reader(raw_data.splitlines(), delimiter=',')
            next(data)
            return data

    def _combine_data(self):
        new_data = []
        for user in self.users:
            new_data.append({"name": user["name"],
                             "gender": user["gender"],
                             "address": user["address"],
                             "books": []})

        new_data_iter = iter(new_data)
        try:
            for book in self.books:
                title, author, _, height, _ = book
                next(new_data_iter)["books"].append({
                    "title": title,
                    "author": author,
                    "height": height
                })
        except StopIteration:
            pass

        return new_data

    def save_data_combination(self, new_file_name: str):
        with open(new_file_name, 'w') as new_file:
            new_data_json = json.dumps(self.data_combination, indent=4)
            new_file.write(new_data_json)


if __name__ == "__main__":
    homework = DataCombiner("users.json", "books-39204-271043.csv")
    homework.save_data_combination('homework')
