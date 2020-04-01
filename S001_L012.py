ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
print(ports)

connections = ((s,d) for s in ports for d in ports)
# print(connections)
#print(len(connections))

connections2 = ((s,d) for s in ports for d in ports if s!=d)
# print(connections2)
#print(len(connections2))

connections3 = ((s,d) for s in ports for d in ports if s < d )
# print(connections3)
#print(len(connections3))

connections_counter = 0
connections_counter2 = 0
connections_counter3 = 0

for x in connections:
    print(x)
    connections_counter = connections_counter + 1

print(connections_counter) 

for x in connections2:
    print(x)
    connections_counter2 = connections_counter2 + 1

print(connections_counter2) 

for x in connections3:
    print(x)
    connections_counter3 = connections_counter3 + 1

print(connections_counter3)