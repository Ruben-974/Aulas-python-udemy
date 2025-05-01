def name_list(name, list_=None):
    if list_ is None:
        list_ = []
    list_.append(name)
    return list_


list_1 = name_list('Jack')
name_list('Anne', list_1)
print(list_1)

list_2 = name_list('Mike')
print(list_2)

