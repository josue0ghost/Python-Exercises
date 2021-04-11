# list definition
movies = ["Batman", "Titanic", "TRON"]
artists = list(('Clairo', 'Eden', 'Drake')) # arg is an iterable
years = list(range(2000, 2050))
variableList = ["str", 5, 4.5, True]

print(movies)
print(artists)
print(years)
print(variableList)

# index
print(movies[1]) # prints 'Titanic'
print(movies[-2]) # with negative index, list is traveled backwards
print(movies[0:2]) # prints range (2 elements in this case)
print(movies[1:])

# add elements to list
movies.append("Blade Runner")

for movie in movies:
    print(f"{movies.index(movie)+1}. {movie}")

# multi-dimensional lists
contact = [
    [
        'Josh',
        'josh.h@gmail.com'
    ],
    [
        'Chiwi',
        'chiwidude@gmail.com'
    ]
]
print(contact)

'''
    other methods
'''
# sorting
contact.sort()
print(contact)

# insert element on index
movies.insert(2, "Mulan")
print(movies)

# delete elements
movies.pop(2) # deleting element at index 2
movies.remove('Titanic')
print(movies)

# reverse list
artists.reverse()
print(artists)

# Is a element in a list?
print('Clairo' in artists)

# length of a list
print(len(artists))

# how many times a element appears in a list
print(years.count(2000))

# add list to a list
movies.extend(artists)
print(movies)