from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import pprint


dir = "C:\\Users\\User\Desktop\mac-dna-seq"
fsa_names =  [x for x in os.listdir(dir) if x.endswith('.fsa')]
#print(fsa_names)
os.chdir(dir)
pprint.pprint(fsa_names)
for name in fsa_names:
    record = SeqIO.read(name,'abi')
    channels = ['DATA1','DATA2','DATA3']
    trace = defaultdict(list)
    for ch in channels:
        trace[ch] = record.annotations['abif_raw'][ch]


    y_int_two = max(trace['DATA2'])
    y_int_three = max(trace['DATA3'])
    x_two = trace['DATA2'].index(y_int_two)
    x_three = trace['DATA3'].index(y_int_three)
    print(x_two,x_three)
    #print(x_three)
# #print(min(trace['DATA1']))
    plt.plot(trace['DATA1'],color='blue')
# #plt.plot(trace['DATA2'],color='red')
    plt.plot(trace['DATA3'],color='green')
# #plt.plot(trace['DATA4'],color='yellow')
    plt.show()
