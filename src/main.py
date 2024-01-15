from functions import five_last, data_convert, modify_card_to, modify_card_from, load_operations

# переменная для функции чтения json
all_operations = load_operations()

# проверка на пустой список
last_operation = []
for i in all_operations:
    if i != {}:
        last_operation.append(i)

# сортировка операций по дате
last_operation.sort(key=lambda x: x.get('date'), reverse=True)

# переменная для функции 5 последних операций
last_list = five_last(last_operation)

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
