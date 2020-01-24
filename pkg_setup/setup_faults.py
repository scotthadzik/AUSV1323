def create_fault_list():

	fault_dict = {
		'open':      {'on_off_relay': True, 'short_relay' :True, 'resist_relay' :True},
		'short':     {'on_off_relay': True, 'short_relay' :False, 'resist_relay' :True},
		'resist': {'on_off_relay': True, 'short_relay' :True , 'resist_relay' :False}
	}

	return fault_dict