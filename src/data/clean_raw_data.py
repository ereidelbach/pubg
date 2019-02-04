#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:45:33 2019

@author: ejreidelbach

:DESCRIPTION:

:REQUIRES:
   
:TODO:
"""
 
#==============================================================================
# Package Import
#==============================================================================
import os  
import pandas as pd
import pathlib
import tqdm

import collections
import matplotlib.pyplot as plt
import math

#==============================================================================
# Reference Variable Declaration
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================
def function_name(var1, var2):
    '''
    Purpose: Stuff goes here

    Inputs   
    ------
        var1 : type
            description
        var2 : type
            description
            
    Outputs
    -------
        var1 : type
            description
        var2 : type
            description
    '''
def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()
    
def plot_scatter(xs, ys1, ys2):
    plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
    plt.scatter(xs, ys2, marker='.', color='gray',  label='ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc=9)
    plt.show()

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def mean(x):
    return sum(x) / len(x)

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def get_column(A, j):
    return [A_i[j] for A_i in A]

def standard_deviation(x):
    return math.sqrt(variance(x))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
    
#==============================================================================
# Working Code
#==============================================================================

#from aggregate_CFBStats_by_category import aggregate_data_by_category

# Set the project working directory
#path_project = pathlib.Path(__file__).resolve().parents[2]
#os.chdir(path_project)
    
path_dir = pathlib.Path('/home/ejreidelbach/Projects/kagglePUBG/data/raw')
os.chdir(path_dir)

df = pd.read_csv('train_V2.csv', nrows=10000)

plot_histogram(df['kills'], 1)
plot_scatter(df, df['kills'], df['winPlacePerc'])