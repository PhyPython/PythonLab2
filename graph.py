
import matplotlib.pyplot as plt

# DataFrameUtilities Class definition
class Graph:

    # DrawScatterGraph
    def DrawScatterGraph(index, x, y, xLabel, yLabel, title, gridLines):
        graph = plt.figure(index)
        plt.scatter(x, y)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.grid(gridLines)
        graph.show()

    # DrawHistGraph
    def DrawHistGraph(index, x, bin, xLabel, yLabel, title, gridLines, facecolor='green', alpha=0.75):
        graph = plt.figure(index)
        plt.hist(x, bin, facecolor='green', alpha=0.75)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.grid(gridLines)
        graph.show()