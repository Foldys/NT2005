# Inputs: r - 2D matrix of responses (time bins by trials)
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
def plot_raster(r, tm, figH, sp):    
    import numpy as np    
    import matplotlib.pyplot as plt
    ax = figH.add_subplot(sp)
    for t in range(0, r.shape[1]): # loop on trials
        spk = r[:, t]
        ax.plot(tm[spk > 0], t*np.ones(sum(spk>0)), 'b.')                
        plt.xlim((tm[0], tm[-1]))

        
# Inputs: r - 2D matrix of responses (time bins by trials)
#         k - number of time bins to average across for PSTH
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
def plot_psth(r, k, tm, figH, sp):    
    r = r.mean(axis = 1)
    psth = r
    if k > 1:
        for t in range(0, r.size):        
            # First attempt, directly according to the definition of a smoothed PSTH: r[round(t-k/2):round(t+k/2)].mean() 
            # This however will go beyond the limit of the array r. Hence, we use min() and max()                  
            psth[t] = r[max(0, round(t-k/2)):min(r.size, round(t+k/2))].mean()    
    ax = figH.add_subplot(sp)    
    ax.plot(tm, psth, 'b') 


# Inputs: rsp - 3D matrix of responses (conditions by time bins by trials)
#         k - number of time bins to average across for PSTH
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
def plot_psths(rsp, k, tm, figH, sp):   
    import matplotlib.pyplot as plt
    ax = figH.add_subplot(sp)
    for c in range (0, len(rsp)): # loop on conditions
        r = rsp[c, :, :].mean(axis = 1)
        psth = r
        if k > 1:
            for t in range(0, r.size):        
                psth[t] = r[max(0, round(t-k/2)):min(r.size, round(t+k/2))].mean() 
        # normalise to show it in spikes/s, we presume all bins are equal size
        psth = psth/(tm[1] - tm[0])*1000                        
        ax.plot(tm, psth, '.-', label='resp. '+str(c))
    ax.legend()
    plt.xlabel('Time (ms)')
    plt.ylabel('spikes/s')
        
        
        
    
        
    
           