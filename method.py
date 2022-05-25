# Примеры методов для списка, строки, множеств, словаря

list_sample=[1, 2, 3, 4, 5]
list_sample.append(6)
print(list_sample)
list_sample.insert(2, -1)
print(list_sample)
list_sample.remove(2)
print(list_sample)
list_sample.pop(2)
print(list_sample)
list_sample.clear()
print(list_sample)

#append(6),insert(2,-1) remove(2),pop(2),clear()

str_sample="Max Jane Kate"
print(str_sample.split(" "))
print(str_sample.find("Ka"))
print(str_sample.lower())
print(str_sample.endswith("lte"))
print(str_sample.replace(" ",","))
#split(" "),find("Ka"),lower(),endswith("lte"),replace(" ",",")

set_sample={'a', 'b', 'c', 'd'}
set_other_sample={'a', 'e'}
set_sample.add("f")
print(set_sample)
set_sample.remove('f')
print(set_sample)
print(set_sample.isdisjoint(set_other_sample) )
print(set_sample.issuperset(set_other_sample))
print(set_sample.union(set_other_sample))


dict_sample = {'key1': 2, 'key2': 4, 'key3': 9}

print(dict_sample.items())
print(dict_sample.keys() )
print(dict_sample.pop('key1') )
print(dict_sample)
print(dict_sample.get('key1',7))
dict_sample.clear()
print(dict_sample)