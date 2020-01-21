from pkg_setup.Fault import Fault

def create_fault_list():
	fault_list = []

	fault_dict = {
		'open': {'fault_relay': True, 'short_relay' :False, 'short_relay' :False},
		'open': {'fault_relay': True, 'short_relay' :False, 'short_relay' :False}
	}

	open_circuit_fault = Fault('Open Circuit Fault', True, False, False)
	hi_res_circuit_fault = Fault('High Resistance Circuit Fault', True, False, True)
	short_circuit_fault = Fault('Open Circuit Fault', True, True, False)

	fault_list.append(open_circuit_fault)
	fault_list.append(hi_res_circuit_fault)
	fault_list.append(short_circuit_fault)
	return fault_dict