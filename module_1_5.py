immutable_va = 'blue', 'red', 'green'
print(immutable_va)
#immutable_va[0] = 'yellow'-кортеж не поддерживает обращение по элементам
mutable_list = ['blue', 'red', 'green']
print(mutable_list)
mutable_list[0]='yellow'
print(mutable_list)
mutable_list.append('yellow')
print(mutable_list)
