# PythonLab2

You can open the file PythonLab2 in Spyder to run everything. (PythonLab2 file is supposed to be the main entry point of where we start our application this uses the class Lab2 which is in the file Lab2.py which has 3 methods Part1, Part2 and Part3)

there is 3 class files that help with seperating out the functionality so it can be re-used by passing in a dataframe.

columnMetaData - is a class that holds some extra information about the column like min, max, nullvalue counts ... etc (this makes it easier to use the data later on because we stored a reference to them)

dataFrameUtilities - this is a class that has some functions to help read/extracting out the dataframe data. Its extracted out into a class so we can re-use them. Ideally there not supposed to be static methods but there is no real benefit of using them as concrete methods for now. The real approach to this is it is supposed to be a library so you can pass it on to someone else and they can just get the answer out by passing in a data frame).
graph - helps draw a graph because we do that alot in this lab.
