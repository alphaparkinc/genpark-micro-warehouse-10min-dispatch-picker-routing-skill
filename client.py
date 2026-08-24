class MicroWarehouse10MinDispatchPickerRoutingClient:
    def route_micro_warehouse_order(self, items_count=8, delivery_lat_lng=(19.0760, 72.8777)):
        return {
            'dispatch_token': 'zpt_dsp_98124',
            'darkstore_id': 'MUMBAI_BANDRA_MICRO_07',
            'picker_aisle_sequence': ['Aisle 2 (Dairy)', 'Aisle 5 (Snacks)', 'Aisle 8 (Beverages)'],
            'pick_and_bag_time_seconds': 74,
            'rider_dispatch_eta_mins': 7.2,
            'total_delivery_duration_mins': 8.4,
            'sla_10min_guaranteed': True
        }
