
# Lab 2

# Count the number of rows in the csv file you've chosen.
# python -m pip install --upgrade pip
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
# python -m pip install xlrd

import sys      # imports the sys module
import pandas as pd

import dataFrameUtilities
from dataFrameUtilities import DataFrameUtilities

import graph
from graph import Graph

# Questions
class Part1:
    def Run():
        print('Running Part1\n')

        # 1. Download the two files and load them into pandas data frames. 
        passengerDataFrame = DataFrameUtilities.ReadFiileToDataframe('passengerData.csv')
        ticketPricesDataFrame = DataFrameUtilities.ReadFiileToDataframe('ticketPrices.xlsx')

        # 2. Merge the two files based on the column they share.
        mergedDataFrame = pd.merge(passengerDataFrame, ticketPricesDataFrame, on='TicketType')
        print(mergedDataFrame)

        # 3. Display the name of the oldest passengers (hint: make use of variables to save some intermediate values).
        maxAge = mergedDataFrame['Age'].max();
        print("Max age: ", maxAge)

        info = mergedDataFrame[mergedDataFrame.Age == maxAge] # gets the oldest person in the list
        print ("Name of oldest person: ", info['Name'].values[0])

        # 4. Plot the data on a scatter plot that shows the Age vs. Ticket Prices
        Graph.DrawScatterGraph(0, mergedDataFrame.Age, mergedDataFrame.Fare, 'Age', 'Fare', 'Part1-Question4', True)

        # 5. Plot only the data that shows female passengers aged 40 to 50 and who paid more than or equal to 40.
        famalePaid40 = mergedDataFrame[(mergedDataFrame.Sex == 'female') & (mergedDataFrame.Age >= 40) & (mergedDataFrame.Age <= 50) & (mergedDataFrame.Fare >= 40)]
        Graph.DrawScatterGraph(1, famalePaid40.Age, famalePaid40.Fare, 'Age', 'Fare', 'Part1-Question5', True)
        
        print('finished part 1\n')

class Part2:
     def Run():
         print('Running Part2\n')

         # 1. Load the slightly modified Titanic survival data into a pandas data frame.
         titanicDataFrame = DataFrameUtilities.ReadFiileToDataframe('titanicSurvival_m.csv')

         # 2. Find the counts of missing values in each column
         # 3. Compute the mean and other descriptive statistics and note these down

         # columnMetaData contains a dictionary of each column of a given dataframe. The min, max, mean, nullvalue counts
         columnMetaData = DataFrameUtilities.GetColumnMetaData(titanicDataFrame)

         # 4. Replace the missing values in "Age" and "Fare" columns with 0 values, and visualise in a scatterplot
         titanicDataFrameWithNoNulls = DataFrameUtilities.GetReplaceNullValues(titanicDataFrame, 0)
         Graph.DrawScatterGraph(2, titanicDataFrameWithNoNulls.Age, titanicDataFrameWithNoNulls.Fare, 'Age', 'Fare', 'Part2-Question4', True)

         # 5. Replace the missing values in "Age" and "Fare" columns with the mean of each column, and visualise in a scatterplot
         titanicDataFrameWithMean = DataFrameUtilities.GetReplaceNullValuesWithMean(titanicDataFrame, columnMetaData)
         Graph.DrawScatterGraph(3, titanicDataFrameWithMean.Age, titanicDataFrameWithMean.Fare, 'Age', 'Fare', 'Part2-Question5', True)
         
         print('finished part 2\n')

class Part3:
     def Run():
         print('Running Part3\n')

         bin = 10

         # 1. Download the csv data file from WHO on Tuberculosis (from Week01). Information on the data can be found on WHO's web page.
         tuberculosisDataFrame = DataFrameUtilities.ReadFiileToDataframe('TB_burden_countries_2014-09-29.csv')

         # 2. You may need to replace missing values before you start.

         # columnMetaData contains a dictionary of each column of a given dataframe. The min, max, mean, nullvalue counts
         columnMetaData = DataFrameUtilities.GetColumnMetaData(tuberculosisDataFrame)

         tuberculosisDataFrameWithMean = DataFrameUtilities.GetReplaceNullValuesWithMean(tuberculosisDataFrame, columnMetaData)
         Graph.DrawHistGraph(4, tuberculosisDataFrameWithMean.e_prev_100k_hi, bin, 'e_prev_100k_hi', 'Frequency', 'Part3-Question3', True)
         
         # 4. Apply a log transformation on the data. Numpy has a log function. and visualise. Observe the changes
         tuberculosisDataFrameAsLog = DataFrameUtilities.GetDataFrameAsLog(tuberculosisDataFrame, columnMetaData)
         Graph.DrawHistGraph(5, tuberculosisDataFrameAsLog.e_prev_100k_hi, bin, 'e_prev_100k_hi', 'Frequency', 'Part3-Question4-Log', True)
     
         # 5. Choose the numerical columns and map all the columns to [0,1] interval (x - min(x) / max(x) - min(x))
         tuberculosisDataFrameScaled = DataFrameUtilities.GetDataFrameScaledToZeroAndOne(tuberculosisDataFrame, columnMetaData)
         
         # 6. Now you can compare the means of each column.
         # print(tuberculosisDataFrameScale)
         print(tuberculosisDataFrameScaled.describe())

         print('finished part 3\n')