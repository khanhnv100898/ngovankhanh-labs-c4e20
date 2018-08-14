def get_even_list(l):
    list_new = []
    for i in l:
        if i % 2 == 0:
            list_new.append(i)

    return list_new


# a = get_even_list([1,4,5,10])
# print(a)