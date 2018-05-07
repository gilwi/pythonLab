from struct import unpack
net = unpack('BBBB' ,b'\n\x00\x00\xff')
print(str(net[0])+'.'+str(net[1])+'.'+str(net[2])+'.'+str(net[3]))
