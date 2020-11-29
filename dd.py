import ipaddress
import time

d = {}
s = set()
begintime = time.time()

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                ipa = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(l)  
                iface = ipaddress.IPv4Interface(ipa)
                ipas = ipa.replace('.', '')
                d[iface] = ipas

# print(hash(iface))
endtime = time.time()
elapsed = endtime - begintime
print("All done")
print(elapsed)