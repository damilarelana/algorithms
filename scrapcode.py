    # initialize dict, with `index 0` being an empty list
    keyDict = 0  # key to store the matching pairs (indexTuple, valueTuple)
    resultPair = list()  # initialize placeholder for matched pairs
    plotDataDict = { 
        keyDict: resultPair,
    }





def getArrayPlotData(arrayWhileSorting: list, plotDataDict: dict):
    cStateOfArray = [(index, value) for index, value in enumerate(arrayWhileSorting)]  # generate current state of the array
    indexTuple, valueTuple = zip(*cStateOfArray)
