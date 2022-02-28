# обработать список ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после
# элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list_2 = []
for elem in my_list:
    if elem.isdigit():
        my_list_2.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+')) and elem[1:].isdigit():
        my_list_2.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        my_list_2.append(elem)

out_info = ' '.join(my_list_2)
print(out_info)
