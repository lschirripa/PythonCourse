dictionary = {  'LOL': "laugh out loud",
                'IDK': "I dont know",
                'TBH': "to be honest"}

print(dictionary)

dictionary['BAU'] = 'business as usual'

print(dictionary)

del dictionary['LOL']

print(dictionary)

emptyVariable = dictionary.get('AF')

if emptyVariable:
    print(emptyVariable)
else:
    print('value not found')