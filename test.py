def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

word_freq = {'is'   : [1, 3, 4, 8, 10],
             'at'   : [3, 10, 15, 7, 9],
             'test' : [5, 3, 7, 8, 1],
             'this' : [2, 3, 5, 6, 11],
             'why'  : [10, 3, 9, 8, 12] }
# Append multiple values for existing key 'at'
word_freq = add_values_in_dict(word_freq, 'at', [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
print('Contents of the dictionary: ')
print(word_freq)