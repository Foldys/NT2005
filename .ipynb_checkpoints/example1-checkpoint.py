from importData import importData
import matplotlib.pyplot as plt
D = importData()

s = 6
D = D[s] # pick recording session s

print('In session ' + str(s) + ' there are ' + str(D['spikes'].shape[0]) + ' neurons, ' + \
      str(D['spikes'].shape[1]) + ' conditions, ' + \
      str(D['spikes'].shape[2]) + ' time bins and ' + \
      str(D['spikes'].shape[3]) + ' trials (repeats)')

n = 9 # neuron
c = 2 # condition
t = 6 # trial

# plot a single trial of one neuron (in a particular stimulation condition)
plt.figure(0)
plt.plot(D['times'], D['spikes'][n,c,:,t])
plt.xlabel('Time (ms)')
plt.ylabel('#spikes')
plt.title('Session: ' + str(s) + ', neuron: ' + str(n) + \
                 ', trial: ' + str(t) + \
                 ', condition: ' + str(D['conditions'][c]))


# plot the total number of spikes per each trial for one condition
plt.figure(1)
plt.plot(D['spikes'][n,c,:,:].sum(axis=0))
plt.xlabel('Trial')
plt.ylabel('#spikes')
plt.title('Session: ' + str(s) + ', neuron: ' + str(n) + \
                 ', total number of spikes in each trial of condition: ' + str(D['conditions'][c]))
           