
import numpy as np
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

import columnMetaData
from columnMetaData import ColumnMetaData

# DataFrameUtilities Class definition
# Additional functions to help with using dataframes
class DataFrameUtilities:

    # Read file into Dataframe if the file cannt be read returns None
    #
    # Returns a new DataFrame
    # filepath [string] - the path of the file
    # sheetName [string] - optional, sheetname for .xlsx files 
    def ReadFiileToDataframe(filePath, sheetName = 'Sheet1'):
        dataframe = None
        try:
            if filePath.endswith('.csv'):
                dataframe = pd.read_csv(filePath) 
            elif filePath.endswith('.xlsx'):
                dataframe = pd.read_excel(filePath, sheetName)
        except:
            print('Failed to read file ', filePath)
        return dataframe

    # Returns a new dataframe replacing all null values with a newValue
    #
    # Returns a new DataFrame
    # dataframe [dataframe] - the dataframe from pandas library
    # newValue [object] - new value to replace null value with in in each cell
    def GetReplaceNullValues(dataframe, newValue):
       dataFrameWithNewValue = dataframe.copy()

       columNames = dataframe.columns
       for index, row in dataframe.iterrows():
           for columnName in columNames:
              cellValue = row[columnName]
              if(pd.isnull(cellValue)):
                dataFrameWithNewValue.at[index, columnName] = newValue
       # return the new dataframe
       return dataFrameWithNewValue
    
    # Returns a new dataframe replacing all null values with the mean
    #
    # Returns a new DataFrame
    # dataframe [dataframe] - the dataframe from pandas library
    # columnMetaDatas [dictionary of <columnName, ColumnMetaData>] - the columnMetaData with the mean for each column
    def GetReplaceNullValuesWithMean(dataframe, columnMetaDatas):
       dataFrameWithMean = dataframe.copy()

       columNames = dataframe.columns
       for index, row in dataframe.iterrows():
           for columnName in columNames:
              cellValue = row[columnName]
              if(pd.isnull(cellValue)):
                columnMetaData = columnMetaDatas[columnName]
                dataFrameWithMean.at[index, columnName] = columnMetaData.mean
       
       # return the new dataframe
       return dataFrameWithMean

    # Returns a dictionary of columnNames and the number of null values
    #
    # Returns a dictionary <columName, count>
    # dataframe [dataframe] - the dataframe from pandas library
    def GetNullValueCount(dataframe):
        columnCounts = { }
        for column in dataFrame.columns:
            columnCounts[column] = 0

        columNames = dataframe.columns
        for index, row in dataframe.iterrows():
            for columnName in columNames:
                if(pd.isnull(cellValue)):
                  columnCounts[columnName] += 1  
        return columnCounts

    # Returns the number of null values in a column
    #
    # Returns a integer
    # dataframe [dataframe] - the dataframe from pandas library
    # columName [string] - the columnName
    def GetNullValueCount(dataframe, columnName):
        count = 0
        for cellValue in dataframe[columnName]:
            if(pd.isnull(cellValue)):
              count += 1
        return count

    # Returns a new dataframe with log applied to all numeric cell values
    #
    # Returns a new dataframe
    # dataframe [dataframe] - the dataframe from pandas library
    def GetDataFrameAsLog(dataframe, columnMetaDatas):
        dataframeAsLog = dataframe.copy()

        columNames = dataframe.columns
        for index, row in dataframe.iterrows():
           for columnName in columNames:
              cellValue = row[columnName]
              columnMetaData = columnMetaDatas[columnName]

              # ignore non numeric fields and zeros
              if (columnMetaData.isNumeric == False or cellValue == 0):
                  continue

              logValue = np.log(cellValue)
              dataframeAsLog.at[index, columnName] = logValue

        return dataframeAsLog

    # Returns a new dataframe scaled to 0 and 1
    #
    # Returns a new dataframe
    # dataframe [dataframe] - the dataframe from pandas library
    def GetDataFrameScaledToZeroAndOne(dataframe, columnMetaDatas):
        dataframeScaled = dataframe.copy()

        columNames = dataframe.columns
        for index, row in dataframe.iterrows():
           for columnName in columNames:
              cellValue = row[columnName]
              columnMetaData = columnMetaDatas[columnName]

              # ignore non numeric fields and zeros
              if (columnMetaData.isNumeric == False or cellValue == 0):
                  continue

              columnMetaData = columnMetaDatas[columnName]
              reScaledValue = DataFrameUtilities.__Rescale(cellValue, columnMetaData.minimum, columnMetaData.maximum)
              dataframeScaled.at[index, columnName] = reScaledValue

        # Return the scaled dataframe
        return dataframeScaled

    # Private Scaling function
    #
    # Returns a float
    # value [value] - the value to scale
    # min [int,float] - the minimum value
    # max [int,float] - the maximum value
    def __Rescale(value, min, max):
        normalized = (value-min)/(max-min)
        return normalized

    # Returns a dictionary of columnMetaData
    #
    # Returns a dictionary <columName, columnMetaData>
    # dataframe [dataframe] - the dataframe from pandas library
    def GetColumnMetaData(dataframe):
        columnMetaDatas = { }
        for column in dataframe.columns:
            isNumeric = False
            minimum = None
            maximum = None
            mean = None
            nullValueCount = DataFrameUtilities.GetNullValueCount(dataframe, column)

            if(dataframe[column].dtype == np.float64 or dataframe[column].dtype == np.int64):
                isNumeric = True
                minimum = dataframe[column].min();
                maximum = dataframe[column].max();
                mean = dataframe[column].mean()
        
            columnMetaData = ColumnMetaData(column, isNumeric, minimum, maximum, nullValueCount, mean)
            columnMetaDatas[column] = columnMetaData

        return columnMetaDatas