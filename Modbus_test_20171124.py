from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('192.168.27.44', 502)
client.connect()

print ('==== AI ====')
#-- FC04: read multi-input registers (3xxxx), for AI
#read_input_registers(start_addr, count, unit=sid)
rr = client.read_input_registers(0,1, unit=1) #read AI
print (rr, "value=", rr.registers)
rr = client.read_input_registers(0,2, unit=1) #read AI
print (rr, "value=", rr.registers)

print ('==== AO ====')
#-- FC03: read multi-registers (4xxxx) for AO
#read_holding_registers(start_addr, count, unit=sid)
rr = client.read_holding_registers(0,1, unit=1) #read AO
print (rr, "value=", rr.registers)
rr = client.read_holding_registers(0,2, unit=1) #read AO
print (rr, "value=", rr.registers)

#-- FC16: write multi-registers for AO
# write_registers(start_addr, value_array, unit=sid)
rq = client.write_registers(0, [10, 20], unit=1)
assert(rq.function_code < 0x80)#if FC>0x80 --> Error
# read back, to check value
rr = client.read_holding_registers(0,4, unit=1) #read AO
print (rr, "AO value=", rr.registers)

print ('==== DI ====')
#-- FC2  Read multi-input discrete ( 1xxxx ) for DI
#   01 02 00 01 00 08 28 0C
#   01 82 01 81 60
# read_discrete_inputs(start_addr, bit count, unit=sid)
rr = client.read_discrete_inputs(0, 4, unit=1) #will reply 1 byte --> 8 bits
print (rr, "DI value=", rr.bits)
rr = client.read_discrete_inputs(0, 10, unit=1)#will reply 2 byte --> 16 bits
print (rr, "DI value=", rr.bits)

print ('==== DO ====')
#-- FC01: Read multi-coils status (0xxxx) for DO
# read_coils(start_addr, bit count, unit=sid)
rr = client.read_coils(0, 1, unit=1)
print (rr, "DO value=", rr.bits[1])
#if error : Exception Response(129, 1, IllegalFunction)
#   01 01 00 00 00 01 FD CA
#   01 81 01 81 90

#-- FC05: Write single-coil (0xxxx) for DO
# read_coils(start_addr, bit count, unit=sid)
print ('-- write single DO --')
rq = client.write_coil(0, True, unit=1)
print (rq)
rr = client.read_coils(0, 4, unit=1)
print (rr, "DO value=", rr.bits)
#if error: Exception Response(129, 1, IllegalFunction)
#   01 05 00 01 FF 00 DD FA
#   01 85 01 83 50

#-- FC15: Write multi-coils ( 0xxxx ) for DO
# write_coils(start_addr, value_array, unit=sid)
print ('-- write multi DO --')
rq = client.write_coils(0, [False]*8, unit=1)
rq = client.write_coils(0, [True]*4, unit=1)
print (rq)
rr = client.read_coils(0, 8, unit=1)
print (rr, "DO value=", rr.bits)

client.close()