import json, os.path
import datetime


def load_operations():
    """список всех операций из json"""
    operations_json = os.path.join('operations.json')
    with open(operations_json, 'r', encoding="utf-8") as file:
        convert_js = json.load(file)
        return convert_js


def five_last(list_opetions):
    """5 последних удачных операций"""
    counter = 0
    last_list = []
    for i in list_opetions:
        if i['state'] == "EXECUTED":
            counter += 1
            last_list.append(i)
            if counter == 5:
                break
    return last_list


def data_convert(i):
        """конвертация даты в нужный формат"""
        data_list = i['date']
        dt = datetime.datetime.fromisoformat(data_list)
        format_date = dt.date().strftime('%d.%m.%Y'), i['description']
        return f'{" ".join(format_date)}'


def modify_card_to(i):
    """конвертация карты получателя в нужный вид """
    name_card_to = i['to'].split()[0]
    card_to = i['to'][-4:].rjust(len(i['to'][-6:]), "*")
    return f'{name_card_to} {card_to}'


def modify_card_from(i):
    """конвертация карты отправителя в нужный вид """
    card_number = i['from'].split()[-1]
    name_card = i['from'].split()[0]
    return f'{name_card} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'

