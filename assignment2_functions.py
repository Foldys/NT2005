# Inputs: r - 2D matrix of responses (time bins by trials)
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
def plot_raster(r, tm, figH, sp):    
    import numpy as np    
    ax = figH.add_subplot(sp)
    for t in range(0, r.shape[1]): # loop on trials
        spk = r[:, t]
        ax.plot(tm[spk > 0], t*np.ones(sum(spk>0)), 'b.')
        


# Inputs: r - 2D matrix of responses (time bins by trials)
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
def plot_simple_psth(r, tm, figH, sp):        
    r = r.mean(axis = 1)    
    ax = figH.add_subplot(sp)    
    ax.plot(tm, r, 'b')



# Inputs: r - 2D matrix of responses (time bins by trials)
#         k - number of time bins to average across for PSTH
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
# Note that this function will NOT work for k = 1 (use plot_simple_psth in this case)
def plot_psth(r, k, tm, figH, sp):    
    r = r.mean(axis = 1)
    psth = r
    for t in range(0, r.size):        
        # First attempt, directly according to the definition of a smoothed PSTH: r[round(t-k/2):round(t+k/2)].mean() 
        # This however will go beyond the limit of the array r. Hence, we use min() and max()                  
        psth[t] = r[max(0, round(t-k/2)):min(r.size, round(t+k/2))].mean()    
    ax = figH.add_subplot(sp)    
    ax.plot(tm, psth, 'b')
    
        
    
    