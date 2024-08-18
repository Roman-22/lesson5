immutable_var = ([1,2,3,4], True)
print(immutable_var)

#immutable_var[3] = 100
#print(immutable_var)   # кортеж не поддерживает обращение по элементам, Поэтому мы не можем добавлять или удалять элементы

mutable_list = ([1,2,3,4,5,6,7])
print(mutable_list)
mutable_list[1] = 0
mutable_list[6] = 33
print(mutable_list)
