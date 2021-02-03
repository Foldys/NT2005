# The function will return an array of dictionaries (with 17 elements). 
# Each element of the array provides data from one recording session. The following keys are defined:
# 'date' - the date of the recording session
# 'subject' - which monkey was recorded
# 'spikes' - 4-dimensional matrix ( neurons x conditions x time x repeats) of spike counts
# 'times' - the times (relative to stimulus onset) of the time dimension (you will see that in all cases it starts from -195ms and goes to 695ms in 10ms increments)
# 'tetrode' - the tetrode on which each neuron was recorded
# 'contamination' - estimate of % of "wrong" spikes (of others neurons) 
# 'conditions' - the stimulus conditions (contrast and orientation)
# The data is provided as MATLAB file this function converts it to the above format
def importData():
    import scipy.io as sio    
    x = sio.loadmat('data_v1_binned_static.mat') # this presumes the file is in the same directory
    x = x['data']
    data = {}
    for i in range(0, len(x)): # loop on recording sessions
        data[i] = {}
        y = x[i][0][0][0] 
        data[i]['date'] = y[0][0]
        data[i]['subject'] = y[1][0]
        data[i]['conditions'] = {} # we deal with y[2][0] below
        data[i]['contamination'] = y[3][0]
        data[i]['tetrode'] = y[4][0]
        data[i]['spikes'] = y[5] # 4-dim array, check out data[i]['spikes'].shape
        data[i]['times'] = y[6][0]   
        z = y[2][0]
        for c in range(0, len(z)):
            data[i]['conditions'][c] = {}
            data[i]['conditions'][c]['contrast'] =  z['contrast'][c][0][0]
            data[i]['conditions'][c]['orientation'] = z['orientation'][c][0][0]
    return data
    
    
    
    