import random
import json
from faker import Faker #pip install Faker
fake = Faker()

first_names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Charlotte', 'Elijah', 'Amelia', 'James', 'Ava', 'William',
               'Sophia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Theodore', 'Harper']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
              'Lopez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee']

first_word = ['The', 'A', 'We']
second_word = ['Octopus', 'Deer', 'Murder', 'Plane', 'Father', 'War', 'Men', 'Never', 'Trial', 'Crime']
third_word = ['Legacy', 'Sorrow', 'Beneath', 'Forever', 'Dragon', 'Fire', 'Ice', 'Blizzard', 'Storm']

genre = ['Action and adventure', 'Art/architecture', 'Alternate history', 'Autobiography', 'Anthology', 'Biography',
         'Chick lit', 'Business/economics', 'Children', 'Crafts/hobbies', 'Classic', 'Cookbook', 'Comic book',
         'Diary', 'Coming-of-age', 'Dictionary', 'Crime', 'Encyclopedia', 'Drama', 'Guide', 'Health/fitness',
         'Fantasy', 'History', 'Graphic novel', 'Home and garden', 'Historical fiction', 'Humor', 'Horror',
         'Journal', 'Mystery', 'Philosophy', 'Poetry', 'Romance', 'Textbook', 'Science fiction', 'Science',
         'Thriller', 'Sports', 'Western', 'Travel', 'Young adult', 'True crime']



book_dict = {}
out_file = open("book_list.json", "w+")
for x in range(1000):
    book_dict[x]=({"Book": random.choice(first_word) + " " + random.choice(second_word) + " " + random.choice(third_word),
                   "ISBN": str(random.randint(1000000000000, 999999999999999)),
                   "Genre": random.choice(genre),
                   "Author": random.choice(first_names) + " " + random.choice(last_names),
                   "DateAdded": str(fake.date_between(start_date='today', end_date='+10y'))})
json.dump(book_dict, out_file, indent = 4)
out_file.close()
