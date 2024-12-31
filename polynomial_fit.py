import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import os
import sys
import time

# ------Generate all terms for a 2D polynomial of given degree-------
def generate_polynomial_terms(degree):
    terms = []
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            terms.append((i, j))
    return terms

# ------Polynomial function of any degree------
def poly_nd(coords, *coeffs):
    x, y = coords
    terms = generate_polynomial_terms(degree)
    result = np.zeros_like(x)
    for (i, j), coeff in zip(terms, coeffs):
        result += coeff * (x ** i) * (y ** j)
    return result

# ------Fit the polynomial using curve_fit------
def rebuild_pt_cloud(points,degree,x_range,y_range):
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
   
    terms = generate_polynomial_terms(degree)
    initial_guess = [0] * len(terms)  # Initial guess for coefficients
    params, _ = curve_fit(poly_nd, (x, y), z, p0=initial_guess)

    # -------Generate the reconstructed pt cloud-------
    x_range = np.linspace(min(x), max(x), 80)
    y_range = np.linspace(min(y), max(y), 50)
    x_grid, y_grid = np.meshgrid(x_range, y_range)
    z_pred = poly_nd((x_grid.ravel(), y_grid.ravel()), *params).reshape(x_grid.shape)

    reconstructed_points = pd.DataFrame({
                                            'x': x_grid.ravel(),
                                            'y': y_grid.ravel(),
                                            'z': z_pred.ravel()     })
    return reconstructed_points


if __name__=='__main__': 
    start = time.time()
    
    # -----parameters----
    degree=9
    range_of_x_new=80
    range_of_y_new=50
    
    #-----create new face points------
    curr_path=os.getcwd()+'\\'
    file_name='c_ori.csv'
    ori_points = np.loadtxt(curr_path+'\\pts\\' +file_name, delimiter=",")
    new_pts=rebuild_pt_cloud(ori_points, degree, range_of_x_new, range_of_y_new)
    
    #-----write new pts to csv------
    output_filename=file_name[0:-4] + '_' + str(degree)+'_degree.csv'
    np.savetxt(curr_path+'\\pts\\'+output_filename, new_pts, delimiter=',')
    
    end = time.time()
    print('new pt_cloud generated, '+str(degree)+ ' degree matching takes '+(str(round((end - start),1))+' seconds'))



