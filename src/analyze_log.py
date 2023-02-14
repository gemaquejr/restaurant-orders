import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        with open(path_to_file, 'r') as file:
            content = csv.reader(file)
            list = [index for index in content]

        with open('data/mkt_campaign.txt', 'w') as file:
            file.write(
                f"{num_orders_for_maria(list)}\n"
                f"{count_arnaldos_hamburguer(list)}\n"
                f"{never_plates_orders_by_joao(list)}\n"
                f"{not_visit_by_joao(list)}"
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


# Referência - https://datagy.io/python-get-dictionary-key-with-max-value/
def num_orders_for_maria(data):
    count = {}
    request_by_maria = [index for index in data if index[0] == 'maria']

    for index in request_by_maria:
        if index[1] not in count:
            count[index[1]] = 1
        else:
            count[index[1]] += 1

    most_requested = max(count, key=count.get)
    return most_requested


def count_arnaldos_hamburguer(data):
    count_hamburguer = 0

    for index in data:
        if index[0] == 'arnaldo' and index[1] == 'hamburguer':
            count_hamburguer += 1
    return count_hamburguer


def never_plates_orders_by_joao(data):
    all_plates = set()
    never_plates_orders = set()

    for index in data:
        all_plates.add(index[1])
        if index[0] == 'joao':
            never_plates_orders.add(index[1])
    return all_plates.difference(never_plates_orders)


def not_visit_by_joao(data):
    days_of_the_week = set()
    not_visit = set()

    for index in data:
        days_of_the_week.add(index[2])
        if index[0] == 'joao':
            not_visit.add(index[2])
    return days_of_the_week.difference(not_visit)
