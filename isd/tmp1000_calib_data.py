# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:49:21 2017

@author: Teshan Shanuka J
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calculate(ref, rd, drawplots=False):
    print("\nWITH ALL POINTS")
    print("\nLinear regression")
    A = np.vstack([rd, np.ones(len(rd))]).T
    m, c = np.linalg.lstsq(A, ref)[0]
    # print(m, c)
    out = m*rd + c

    diff = out - ref
    # print("mean: %.3f \n std: %.3f" % (np.mean(diff), np.std(diff)))
    # print("SIGMA: ", str(np.sqrt(np.std(diff)**2 + 0.1**2)))

    df = pd.DataFrame(data={'ref':ref, 'read':rd, 'out':out, 'err':diff}, columns=['ref', 'read', 'out', 'err'])
    # print(df)

    print("\nError\tmean: ", df.err.mean())
    print("\tstd:  ", df.err.std(ddof=0))
    print("Needed ref sigma (for CI 95%) :", np.sqrt(0.05**2 - df.err.std(ddof=0)**2))

    ############################################

    print("\nPolynomial Regression (deg-2)")
    z = np.polyfit(rd, ref, 2)
    p = np.poly1d(z)
    df['out_p'] = p(rd)
    df['err_p'] = df['out_p'] - ref
    # print(df)

    print("\nError\tmean: ", df.err_p.mean())
    print("\tstd:  ", df.err_p.std(ddof=0))
    print("Needed ref sigma (for CI 95%) :", np.sqrt(0.05**2 - df.err_p.std(ddof=0)**2))

    if drawplots:
        plt.figure()
        plt.plot(rd, ref, 'o', label='Original data', markersize=10)
        plt.plot(rd, out, 'r', label='Fitted line')
        poly_x = np.linspace(25, 50, 100)
        poly_y = p(poly_x)
        plt.plot(poly_x, poly_y, 'g', label='Fitted poly' )
        plt.legend()

def calib(calib_ref, calib_rd, ref, rd, drawplots=False):
    print("\nWITH %d POINTS" % calib_ref.shape[0])
    print("\nLinear regression")
    A = np.vstack([calib_rd, np.ones(len(calib_rd))]).T
    m, c = np.linalg.lstsq(A, calib_ref)[0]
    # print(m, c)
    out = m*rd + c

    diff = out - ref

    df = pd.DataFrame(data={'ref':ref, 'read':rd, 'out':out, 'err':diff}, columns=['ref', 'read', 'out', 'err'])
    # print(df)

    print("\nError\tmean: ", df.err.mean())
    print("\tstd:  ", df.err.std(ddof=0))
    print("Needed ref sigma (for CI 95%) :", np.sqrt(0.05**2 - df.err.std(ddof=0)**2))

    ############################################

    print("\nPolynomial Regression (deg-2)")
    z = np.polyfit(calib_rd, calib_ref, 2)
    p = np.poly1d(z)
    df['out_p'] = p(rd)
    df['err_p'] = df['out_p'] - ref
    # print(df)

    print("\nError\tmean: ", df.err_p.mean())
    print("\tstd:  ", df.err_p.std(ddof=0))
    print("Needed ref sigma (for CI 95%) :", np.sqrt(0.05**2 - df.err_p.std(ddof=0)**2))

    if drawplots:
        plt.figure()
        plt.plot(rd, ref, 'o', label='Original data', markersize=10)
        plt.plot(rd, out, 'r', label='Fitted line')
        poly_x = np.linspace(25, 50, 100)
        poly_y = p(poly_x)
        plt.plot(poly_x, poly_y, 'g', label='Fitted poly' )
        plt.legend()

def calib_linear(calib_ref, calib_rd, ref, rd, drawplots=False):
    A = np.vstack([calib_rd, np.ones(len(calib_rd))]).T
    m, c = np.linalg.lstsq(A, calib_ref)[0]
    # print(m, c)
    out = m*rd + c

    diff = out - ref

    df = pd.DataFrame(data={'ref':ref, 'read':rd, 'out':out, 'err':diff}, columns=['ref', 'read', 'out', 'err'])
    # print(df)
    std = df.err.std(ddof=0)
    std_ref = np.sqrt(0.05**2 - std**2)
    print("Error\tmean: ", df.err.mean())
    print("\tstd:  ", std)
    print("Needed ref sigma (for CI 95%) :", std_ref)

    return std, std_ref


ref = np.array([25.,30.,34.,35.,36.,36.5,37.,37.5,38.,39.,40.,45.,50.])
rd = np.array([25.8,30.8,34.9,35.9,36.9,37.4,37.9,38.4,38.9,39.9,40.9,45.8,50.8])


drawplots = False

# calculate(ref, rd, drawplots=drawplots)

######### won't be success unless there are enough data points #############
# calib_indices = [1, 6, 11]
# calib(calib_ref, calib_rd, ref, rd, drawplots=drawplots)
std = []
for i in range(100):
    calib_indices = np.random.choice(range(len(ref)), 3, replace=False)
    # print(calib_indices)
    calib_ref = ref[calib_indices]
    calib_rd = rd[[calib_indices]]
    print(calib_ref)
    std.append(calib_linear(calib_ref, calib_rd, ref, rd, drawplots=drawplots))

stds = list(zip(*std))[0]
stds_ref = list(zip(*std))[1]
print("Mean std for random samples of 3: ", np.mean(stds))
print("Mean reference std needed (ignoring NaNs): ", np.nanmean(stds_ref))

plt.show()
