import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def multiple_corrs_excel(filename, colx, coly=list):
    '''
    Computes correlation coefficients of a list of columns in an Excel file to one particular column. Also creates a plot for each correlation.
    
    ----------
    Example:
    >>>statdoer_version2("Spam_Data.xlsx", "Spam Consumption Frequency", ["Spam Quality", "Love for Eggs", "Frequency of Farts in Your General Direction"])
    The correlation coefficient of Spam Conspumption Frequency and Spam Quality is 0.75.
    
    PLOT APPEARS HERE
    
    The correlation coefficient of Spam Consumption Frequency and Love for Eggs is 0.84.
    
    PLOT APPEARS HERE
    
    The correlation coefficient of Spam Consumption Frequency and Frequency of Farts in Your General Direction is 1.00.
    
    PLOT APPEARS HERE
    
    '''
    
    
    
    DataFrame = pd.read_excel(filename)
    
    for item in coly:
        y = float(DataFrame[colx].corr(DataFrame[item]))
        print("The correlation coefficient of {} and {} is {number:.{digits}f}. \n".format(colx, item, number = y, digits=2))
        corrplot = plt.plot(DataFrame[colx], DataFrame[item], "bo")
        plt.xlabel(colx)
        plt.ylabel(item)
        plt.title(colx + " vs. " + item)
        plt.show()
    
