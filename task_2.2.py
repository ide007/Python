my_list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list_1)
my_list_2 = []
for value in my_list_1:
    if (value.isdigit()) == True:
        my_list_2.append('"'+value.zfill(2)+'"')
    elif '+' in value or '-' in value:
        my_list_2.append('"' + value.zfill(3) + '"')
    else:
        my_list_2.append(value)
print(' '.join(my_list_2))
