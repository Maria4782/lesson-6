immutable_var = 1, 2, 'шаурма', False
print(immutable_var)
#immutable_var[0]=20 (Кортеж - неизменяемый объект и не поддерживает обращение к элементам
# поэтому при попытке его изменения, выдает ошибку)
mutable_list = [10, 20, 'Urban', True]
print(mutable_list)
mutable_list[2]= 'Apple'
mutable_list[1]= 134
print(mutable_list)