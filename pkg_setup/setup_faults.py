def create_fault_list():

	fault_type = {
		'open':      {'on_off_relay': True, 'short_relay' :False, 'resist_relay' :False},
		'short':     {'on_off_relay': True, 'short_relay' :False, 'resist_relay' :True},
		'resist': {'on_off_relay': True, 'short_relay' :True , 'resist_relay' :False}
	}

	return fault_type