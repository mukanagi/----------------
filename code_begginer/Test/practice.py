# filter() = creates collection of elements from an iterable
#              for which a function returns true

# filter(function, iterable)

friends = [("Rachel", 19),
            ("Joe", 16),
            ("Phoebe", 17),
            ("Chandler", 21),
            ("Monica", 20),
            ("Ross", 18)]
        
age = lambda data: data[1] >= 18

adult_friends = list(filter(age, friends))

for i in adult_friends:
    print(i)