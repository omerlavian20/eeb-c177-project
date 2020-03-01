import pandas as pd
import csv
import re

def dummy_coder_excel():
    #(inputfile, variable, cat1, cat2, outputfile)
    '''
    Converts categorical variables with two categories into dichotomous variables and stores the output in a separate text file. This allows categorical variables to be used in a multiple linear regression.
    "category1" is stored as a 0, while "category2" is stored as a 1.
    
    This is a draft function. It will be modified to be more generalizable.
    
    '''
    
    #use regex to make function robust against typos; if wrote hop or fly in past of present tense or in upper or lowecase, then fxn should still work
    #no typos appear in this case, but future variability in data entry will have less of an effect on the function due to this use of regex 
    Dataframe = pd.read_excel("FID_Data.xlsx")
    dummied_list = []
    #iterate through items in category and assign values of 0 or 1 to each entry 
    for item in Dataframe["Flew.hop"]:
        matchtest1 = re.match("[Ff]*", str(item))
        matchtest2 = re.match("[Hh]*", str(item))
        if bool(matchtest1) == True:
            dummied_list.append(0)
        if bool(matchtest2) == True:
            dummied_list.append(1)
        else:
            continue
    #move codes to separate file for future use
    with open("FlewHop_Dummied.txt", "w+") as output:
        for item in dummied_list:
            output.write(str(item) + "\n")
