# Inputs: rsp - 3D matrix of responses (conditions by time bins by trials)
#         k - number of time bins to average across for PSTH
#         tm - 1D vector specifying the times of the time bins (in ms)
#         figH - figure handle
#         sp - subplot in which the raster will be plotted
# Note that this function will NOT work for k = 1 (use plot_simple_psth in this case)
def plot_psths(rsp, k, tm, figH, sp):    
    ax = figH.add_subplot(sp)
    for c in range (0, len(rsp)): # loop on conditions
        r = rsp[c, :, :].mean(axis = 1)
        psth = r
        if k > 1:
            for t in range(0, r.size):        
                psth[t] = r[max(0, round(t-k/2)):min(r.size, round(t+k/2))].mean() 
        # normalise to show it in spikes/s, we presume all bins are equal size
        psth = psth/(tm[1] - tm[0])*1000                        
        ax.plot(tm, psth)
        
        
        
    
        
    
    