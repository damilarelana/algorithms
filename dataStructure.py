def manipulate_data(myDataType, myData):
    if myDataType == "list":
        countDownTimer = len(myData) - 1
        newList = []
        while countDownTimer >= 0:
            newList.append(myData[countDownTimer])
            countDownTimer -= 1
        return newList
    elif myDataType == "dictionary":
        return myData.keys()
    else:
        newSet = {"ANDELA", "TIA", "AFRICA"}
        unionSet = myData | newSet
        return unionSet