ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
print(ports)

connections = [(s,d) for s in ports for d in ports]
# print(connections)
print(len(connections))

connections2 = [(s,d) for s in ports for d in ports if s!=d]
# print(connections2)
print(len(connections2))

connections3 = [(s,d) for s in ports for d in ports if s < d ]
# print(connections3)
print(len(connections3))