[1, 2, ,3, 4]

# Logic for splitting
#   - leftSubList = inputList[inputListLowerIndex:splitIndex+1]
#   - rightSubList = inputList[splitIndex:inputListUpperIndex+1]

Right 
1st Iteration
  inputList = [1, 2, ,3, 4]
  splitIndex = (0 + 3 + 1)// 2 = 2
  leftSubList = [1, 2]
  rightSubList = [3, 4]

2nd Iteration:
  inputList [3, 4]
  inputListLowerIndex = 2
  inputListUpperIndex = 3
  new splitIndex = (2 + 3 + 1) // 2 = 3
  new rightSublist = [4]

3rd Iteration
  inputList [4]
  inputListLowerIndex = 3
  inputListUpperIndex = 3
  new splitIndex = (3 + 3 + 1) // 2 = 3

===========
  
1st Iteration
  inputList = [1, 2, ,3, 4]
  splitIndex = (0 + 3 + 1)// 2 = 2
  leftSubList = [1, 2]
  rightSubList = [3, 4]

2nd Iteration:
  inputList [1, 2]
  inputListLowerIndex = 0
  inputListUpperIndex = 1
  new splitIndex = (0 + 1 + 1) // 2 = 1
  new leftSublist = [1]

3rd Iteration
  inputList [1]
  inputListLowerIndex = 0
  inputListUpperIndex = 0
  new splitIndex = (0 + 0 + 1) // 2 = 0