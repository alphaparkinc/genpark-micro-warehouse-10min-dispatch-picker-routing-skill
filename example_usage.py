from client import MicroWarehouse10MinDispatchPickerRoutingClient

def main():
    client = MicroWarehouse10MinDispatchPickerRoutingClient()
    res = client.route_micro_warehouse_order(6, (19.0800, 72.8800))
    print('Darkstore: ' + res['darkstore_id'] + ' | Pick & Bag: ' + str(res['pick_and_bag_time_seconds']) + 's')
    print('Delivery ETA: ' + str(res['total_delivery_duration_mins']) + ' mins (10-Min SLA: ' + str(res['sla_10min_guaranteed']) + ')')
    print('Aisle Route: ' + ' -> '.join(res['picker_aisle_sequence']))

if __name__ == '__main__':
    main()
