from importData import importData
import matplotlib.pyplot as plt
    

D = importData()
D = D[4] # pick recording session s
n = 3 # neuron
c = 9 # condition with strong response
    
# plot raster for the chosen neuron and condition (in the chosen session)
plt.figure(2)
for t in range(0, D['spikes'].shape[3]): # loop on trials
    spk = D['spikes'][n, c, :, t]
    for tp in range(0, len(D['times'])): # loop on time points
        if spk[tp] > 0:
            plt.plot(D['times'][tp], t, 'b.')
plt.xlabel('Time (ms)')
plt.ylabel('Trial')


# a more efficient/concise way to do the plotting:
import numpy as np
plt.figure(3)
for t in range(0, D['spikes'].shape[3]): # loop on trials
    spk = D['spikes'][n, c, :, t]
    plt.plot(D['times'][spk > 0], t*np.ones(sum(spk>0)), 'b.')
plt.xlabel('Time (ms)')
plt.ylabel('Trial')
    
           