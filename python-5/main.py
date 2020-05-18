from datetime import datetime, time
from collections import defaultdict

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def calculate_bill(start_call, end_call):
    # Definição de variávies constantes
    tax = 0.36
    tax_call = 0.09
    no_fee = 0
    call_in = start_call.time()
    call_out = end_call.time()
    call_time = ((end_call - start_call).total_seconds())//60
    # Definição do datetime com os horários
    call_day = time(6, 0, 0)
    call_night = time(22, 0, 0)
    # Calculos Custos baseado nos horáios
    if call_in >= call_day and call_out <= call_night:
        call_cost = tax_call * call_time + tax
    elif call_in > call_night:
        call_cost = no_fee * call_time + tax
    elif call_in < call_day and call_out < call_day:
        call_cost = no_fee * call_time + tax
    elif call_in < call_day and call_out >= call_day:
        charging = call_out - call_in
        call_cost = tax_call * charging
    elif call_in <= call_night and call_out > call_night:
        charging = call_out - call_in
        call_cost = tax_call * charging + tax

    return call_cost


def classify_by_phone_number(records):
    billings = []
    for record in records:
        calls = {}
        start_call = datetime.fromtimestamp(record['start'])
        end_call = datetime.fromtimestamp(record['end'])

        cost = calculate_bill(start_call, end_call)

        calls['source'] = record['source']
        calls['total'] = cost
        # Registro das Ligações
        billings.append(calls)

    rm_duplicate = defaultdict(int)
    for item in billings:
        rm_duplicate[item['source']] += item['total']
    total_cost = [{'source': source, 'total': float("{:.2f}".format(total))} for source, total in rm_duplicate.items()]
    # Ordena valores pelo maior total
    order_by_cost = sorted(total_cost, key=lambda x: x['total'], reverse = True)

    return order_by_cost
