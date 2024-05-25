L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = {L1[i]: L2[i] for i in range(len(L1))}

print(d)
