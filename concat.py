#************************************************************************************************************************

#  DEPARTMENT     : NA                                                                                                  #

#  NAME           : concat.py                                                                                           #

#  DATA DOMAIN    : ****                                                                                                #

#  FREQUENCY      : NA                                                                                                  #

#  RESTARTABILITY : ****                                                                                                #

#  CONVERSION     : This script is mainly used, to merge CSV files.                                                     #    #                                                                                                                       #

#------------------------------------------------------------------------------------------------------------------------

# MODIFICATION HISTORY                                                                                                  #

#------------------------------------------------------------------------------------------------------------------------

#  DATE        TICKET/STORY        AUTHOR                               COMMENTS                                        #

#------------------------------------------------------------------------------------------------------------------------

# 20210406                         MADAN REDDY                          Initial Version                                 #

#========================================================================================================================

 

import os

import glob

import pandas as pd

 

#Setting the path for CSV Files

path = "C:\\Users\\nt07br\\OneDrive - ING\\Desktop\\CSV file\\"

 

#Joining all the CSV files

join_files = glob.glob(os.path.join(path, "*.csv"))

 

#Parsing data from different CSV files

all_df = []

for f in join_files:

    df = pd.read_csv(f, sep=',')

    df['file'] = f.split('\\')[-1]

    all_df.append(df)

 

df_merged = pd.concat(all_df, ignore_index=True, sort=True )

new_cols = [col for col in df_merged.columns if col != 'file'] + ['file']

df_merged = df_merged[new_cols]

 

#Output file is created

df_merged.to_csv("C:\\Users\\nt07br\\OneDrive - ING\\Desktop\\CSV file\\merged2.csv")

 