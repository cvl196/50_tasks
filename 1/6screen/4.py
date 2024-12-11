names = {'name1':'alex',
        'name2':'matt',
        'name3':'artem',
        'name4':'alice',
        'name5':'bob',
        }
def dicter(dictionary):
    keys = list(dictionary.keys())
    dictionary[keys[0]], dictionary[keys[-1]] = dictionary[keys[-1]], dictionary[keys[0]]
    del dictionary[keys[1]]
    dictionary['new key'] = 'new value'
    return dictionary
print (dicter(names))