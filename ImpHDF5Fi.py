import h5py

filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
data = h5py.File(filename, 'r')
print(type(data))
for key in data.keys():
    print(key)

for key in data ['meta'].keys():
    print(key)

for key in data ['quality'].keys():
    print(key)

print(data['meta']['Description'][()], data['meta']['Detector'][()])
"""LIGO = description sementara H1 = Detector"""
