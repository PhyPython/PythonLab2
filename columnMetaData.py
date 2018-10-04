
# ColumnMetaData Class definition, a wrapper for the columns in a dataframe that holds
# extra information about the column.
class ColumnMetaData:
   # Constructor
   def __init__(self, columnName, isNumeric, minimum, maximum, nullCount, mean):
       
       # The ColumnName
       self.columnName = columnName

       # True if colum is a Numeric data type
       self.isNumeric = isNumeric

       # the minimum value in the column
       self.minimum = minimum

       # The maximum value in the column
       self.maximum = maximum

       # Number of null values
       self.nullCount = nullCount

       # The Mean
       self.mean = mean