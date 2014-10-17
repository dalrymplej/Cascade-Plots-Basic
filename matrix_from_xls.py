def matrix_from_xls(file_w_path,column,xcycle,skip):
    """Reads xls file and produces 2-D matrix
    """
    import numpy as np
    
    data_tmp = np.array(np.genfromtxt(file_w_path, delimiter=',',skip_header=1)) # Read csv file
    data_yr_tmp = data_tmp[:,column]
    numdat = len(data_yr_tmp)
    data_yr = data_yr_tmp[skip:-(xcycle-skip+numdat%xcycle)] # start at skip
    data_2D = np.reshape(np.array(data_yr), (-1,xcycle)) #2D matrix of data in numpy format
    
    return data_2D
