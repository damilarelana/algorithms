
# animate()
#  -
# def animate(i: int, xx, stateDataLists, ax):
def animate(i: int, arrayPlot, stateDataLists):
    arrayPlot.set_height(stateDataLists[i])
    # arrayPlot = ax.bar(xx[0], stateDataLists[i], color='green', alpha=0.8)  # `[0]` helps to ensure that we plot only the first array due to how ax.bar handles 
    return arrayPlot



def setupPlotParams(listMinValue: int, listMaxValue: int, stateDataLists: list):
    # setup plotting area attributes
    #   - set_ylim refers to the the actual values in the array hence why it should be on the y-axis - in relation to a bar chart
    #       + `5` is used to pad the listMinValue and listMaxValue to animating those values easier to see
    #   - set_xlim refers to the index numbers of the array, which can be computed simply from the array length 
    #   - xLinspace is obtained from the global variable scope
    #   - yLinspace is calculated here using attributes of the already sorted list e.g. listMaxValue

    yLinspace = np.linspace(listMinValue, listMaxValue, inputListLength) # creates even space in y-axis for array element values
    xx, yy = np.meshgrid(xLinspace, yLinspace)  # create the mesh grid 

    # figsize = (6, 3)  # set figure size tuple i.e. canvas size (i.e. paper size: A4, Letter, wide-screen aspect ratio etc.)
    fig, ax = plt.subplots(figsize=(6, 3))
    # ax.set(xlim=(0, inputListLength-1), ylim=(listMinValue-5, listMaxValue+5))
    ax.set_xlim(0, inputListLength-1)  # handles the scaling of the axis
    ax.set_ylim(0, listMinValue-5, listMaxValue+5)

    ax.set_xlabel("Index")  # handles the title label for of x-axis
    ax.set_ylabel("Value")  # handles the title label for of y-axis

    ax.set_title(algorithmName)  # handles printing of the name of the overall plot at the top
    
    color='green' # color of each bar chart shape

    pdb.set_trace()

    # plot the first array data
    #   - note that `stateDataLists[0, :]` is acting like `yy` i.e. the height data to the barplot handler
    #   - hence why we later `animate` i.e. iterate of `yy` (i.e. stateDataLists[i, :] different indices) in the `animate()` function
    arrayPlot = ax.bar(xx[0], stateDataLists[0], color, alpha=0.8)  # `[0]` helps to ensure that we plot only the first array due to how ax.bar handles 
    
    return fig, arrayPlot  # return generated plot setup parameters as a tuple




def createAnimation(stateDataLists: list, listMinValue: int, listMaxValue: int, algorithmName: str, animationFormat: str):
    # setup the matplotlib's plot parameters
    fig, arrayPlot = setupPlotParams(listMinValue, listMaxValue, stateDataLists)

    # create animation
    #   - 'interval' talks about ms interval between frames
    #   - 'frames' required to help save the animation later
    #   - 'blit' ensures that only areas of the plot which have changed are re-drawn i.e. improves performance and smoothness
    #   - uses `fig` after setupPlotParams() is called
    #   - calls `animate()` [while using the `stateDataList` and `arrayPlot`] defined within the scope of `createAnimation`
    animation = FuncAnimation(fig, animate(arrayPlot, stateDataLists), interval=200, frames=inputListLength-1, blit=True)

    # show
    plt.draw()
    plt.show()

    # save animation
    #   - checks the animation format
    #   - uses anonymous function to simulate a switch statement
    #   - to save as `mp4` change `filename` assignment i.e. "filename = algorithm + '.mp4' "
    filename = algorithmName + animationFormat
    if animationFormat == "gif":
        animation.save(filename, writer='imagemagick')
    else:
        animation.save(filename)



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()