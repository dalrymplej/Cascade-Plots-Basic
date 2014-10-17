def matrix_from_xls(file_w_path,column):
    """Reads xls file and produces 2-D matrix
    """
    import numpy as np
    
    data_tmp = np.array(np.genfromtxt(file_w_path, delimiter=',',skip_header=1)) # Read csv file
