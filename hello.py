import snap7

IP = '192.168.0.1'
RACK = 0
SLOT = 1
DB_NUMBER = 100
START_ADDRESS = 0
SIZE = 259
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cpu_info()
print(f'Module Type: {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'State: {state}')
print(plc.get_cpu_state)

db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
