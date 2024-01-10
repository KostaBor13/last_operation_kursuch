import json, os.path
import datetime


def load_operations():
    """список всех операций"""
    operations_json = os.path.join('src','operations.json')
    with open(operations_json, 'r', encoding="utf-8") as file:
        convert_js = json.load(file)
        return convert_js


convert_js = load_operations()


def five_last():
    counter = 0
    last_list = []
    for i in convert_js:
        if i['state'] == "EXECUTED":
            counter += 1
            last_list.append(i)
            if counter == 5:
                break
    return last_list


last_list = five_last()

last_list.sort(key=lambda x: x.get('date'), reverse=True)


for i in last_list:
    data_list = i['date']
    dt = datetime.datetime.fromisoformat(data_list)
    if i.get('from'):
        card_number = i['from']

        name_card = card_number.split()[0]
        card_show = card_number.split()[-1]
        private_number = card_show[:6] + (len(card_show[6:-4]) * '*') + card_show[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4

        card_show_to = i['to']
        name_card_to = card_show_to.split()[0]
        card_to = i['to'][-4:].rjust(len(i['to'][-6:]), "*")

        print(dt.date().strftime('%d.%m.%Y'), i['description'])
        print(name_card," ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]),"->", name_card_to, card_to)
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print()
    else:
        print(dt.date().strftime('%d.%m.%Y'), i['description'])
        print(name_card_to, card_to)
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        print()