#№1
basketball_players = {}

def add_player(name, height):
    basketball_players[name] = height

def delete_player(name):
    if name in basketball_players:
        del basketball_players[name]

def find_player(name):
    return basketball_players.get(name)

def update_player(name, height):
    if name in basketball_players:
        basketball_players[name] = height



#№2

eng_fr = {}

def add_word(eng, fr):
    eng_fr[eng] = fr

def delete_word(eng):
    if eng in eng_fr:
        del eng_fr[eng]

def find_word(eng):
    return eng_fr.get(eng)

def update_word(eng, fr):
    if eng in eng_fr:
        eng_fr[eng] = fr



#№3

company_workers = {}

def add_worker(name, phone, email, position, room, skype):
    company_workers[name] = {
        "phone": phone,
        "email": email,
        "position": position,
        "room": room,
        "skype": skype
    }

def delete_worker(name):
    if name in company_workers:
        del company_workers[name]

def find_worker(name):
    return company_workers.get(name)

def update_worker(name, field, value):
    if name in company_workers and field in company_workers[name]:
        company_workers[name][field] = value


#№4

books = {}

def add_book(title, author, genre, year, pages, publisher):
    books[title] = {
        "author": author,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher
    }

def delete_book(title):
    if title in books:
        del books[title]

def find_book(title):
    return books.get(title)

def update_book(title, field, value):
    if title in books and field in books[title]:
        books[title][field] = value



#test

# Task 1
add_player("Kobe Bryant", 198)
add_player("Michael Jordan", 198)
update_player("Kobe Bryant", 197)
delete_player("Michael Jordan")
print("№1", find_player("Kobe Bryant"))

# Task 2
add_word("cat", "chat")
add_word("dog", "chien")
print("№2", find_word("cat"), find_word("dog"))
update_word("dog", "le chien")
delete_word("cat")
print("№2", find_word("dog"))

# Task 3
add_worker("John Smith", "12345", "john@mail.com", "Manager", "101", "john_s")
print("№3", find_worker("John Smith"))
update_worker("John Smith", "room", "202")
print("№3", find_worker("John Smith"))
delete_worker("John Smith")


# Task 4
add_book("Harry Potter", "J.K. Rowling", "Fantasy", 1997, 350, "Bloomsbury")
update_book("Harry Potter", "pages", 367)
print("№4", find_book("Harry Potter"))
delete_book("Harry Potter")
