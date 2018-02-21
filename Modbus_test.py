"""""
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.11.51', 503)
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
print()
client.close()

"""""

a = [['Job','mx'],[1, 2]]
print(a[0][0])

