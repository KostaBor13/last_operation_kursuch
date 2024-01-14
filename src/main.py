from functions import five_last, data_convert, modify_card_to, modify_card_from, load_operations

# переменная для функции чтения json
all_operations = load_operations()

# создание списка из json для работы
list_opetions = []
for i in all_operations:
    list_opetions.append(i)

# переменная для функции 5 последних операций
last_list = five_last(list_opetions)

# сортировка операций по дате
last_list.sort(key=lambda x: x.get('date'), reverse=True)

# Вывод итоговой информации
for i in last_list:
    if i.get('from'):
        print()
        print(data_convert(i))
        print(modify_card_from(i), '->', modify_card_to(i))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])

    else:
        print()
        print(data_convert(i))
        print(modify_card_to(i))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
