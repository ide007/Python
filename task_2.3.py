my_list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list_1))
for idx, value in enumerate(my_list_1):
    if value.isdigit() == True:
        my_list_1[idx] = ('"' + value.zfill(2) + '"')
    elif '+' in value or '-' in value:
        my_list_1[idx] = ('"' + value.zfill(3) + '"')
print(' '.join(my_list_1))
print(id(my_list_1))
