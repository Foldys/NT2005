from importData import importData
from assignment2_functions import plot_raster
import matplotlib.pyplot as plt

# --------------- Part 1: plotting a raster for several stimuli 

    
# Note that here just one neuron is plotted (in 4 different conditions).
# This code can be replicated (or enacpsulated into a function) to do so for 2 more neurons.
D = importData()
D = D[4] # pick recording session s
n = 3 # neuron

figH = plt.figure(0)
for i in range(0, 4): # loop on 4 different conditions
    c = 3+2*i # condition
    plot_raster(D['spikes'][n, c, :, :], D['times'], figH, 411+i)
    print('plotted raster for condition ' + str(c) + ' : ' + str (D['conditions'][c]))
plt.xlabel('Time (ms)')
plt.ylabel('Trial')

# --------------- Parts 2 & 3: plotting a psth 
from assignment2_functions import plot_simple_psth, plot_psth
figH1 = plt.figure(1)
figH5 = plt.figure(2)
for i in range(0, 4): # loop over 4 different conditions
    c = 3+2*i
    plot_simple_psth(D['spikes'][n, c, :, :], D['times'], figH1, 411+i)
    plot_psth(D['spikes'][n, c, :, :], 5, D['times'], figH5, 411+i)
    print('plotted PSTH for condition ' + str(c) + ' : ' + str (D['conditions'][c]))
plt.xlabel('Time (ms)')

