def create_fault_list():

	fault_dict = {
		'open':      {'fault_relay': True, 'short_relay' :False, 'resist_relay' :False},
		'short':     {'fault_relay': True, 'short_relay' :False, 'resist_relay' :True},
		'hi_resist': {'fault_relay': True, 'short_relay' :True , 'resist_relay' :False}
	}

	return fault_dict