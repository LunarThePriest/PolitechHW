favourites = {'color': 'brown', 'fruit': 'banana', 'drinks': ['hot chocolate', 'tea'], 'dct': {1: 1, 2: 2}}

print(favourites['color'])
print(favourites.get('instrument', 'Not Found'))

favourites['instrument'] = 'violin'
favourites.update({'color': 'deep blue', 'tea': 'black'})

fruit = favourites.pop('fruit')
del favourites['drinks']



print(favourites)
print(fruit)
