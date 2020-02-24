#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#input file to analyze, column that want to compare other columns to, and list of columns that want to compare to the original column
def multiple_corrs_excel(filename, colx, coly):
    '''
    Computes correlation coefficients of a list of columns in an Excel file to one particular column. Also creates a plot for each correlation.
    
    ----------
    Example:
    >>>multiple_corrs_excel("Spam_Data.xlsx", "Spam Consumption Frequency", ["Spam Quality", "Love for Eggs", "Frequency of Farts in Your General Direction"])
    The correlation coefficient of Spam Conspumption Frequency and Spam Quality is 0.75.
    The correlation coefficient of Spam Consumption Frequency and Love for Eggs is 0.84.
    The correlation coefficient of Spam Consumption Frequency and Frequency of Farts in Your General Direction is 1.00.
    
    '''
    
    
    assert type(coly) == list, "The third input must be in the format of a list."
    #turn an Excel file into a Pandas dataframe
    DataFrame = pd.read_excel(filename)

    #iterate through list of columns, compute Pearson's correlation coefficient of each column with original column, and print out a a statement with the correlation coefficient as well as a plot relating each pair of columns 
    for item in coly:
        y = float(DataFrame[colx].corr(DataFrame[item]))
        print("The correlation coefficient of {} and {} is {number:.{digits}f}. \n".format(colx, item, number = y, digits=2))
        corrplot = plt.plot(DataFrame[colx], DataFrame[item], "bo")
        plt.xlabel(colx)
        plt.ylabel(item)
        plt.title(colx + " vs. " + item)
        plt.show()
    

multiple_corrs_excel("FID_Data.xlsx", "FID (m)", ["DistanceFromCover", "Conspecifics Present"])


