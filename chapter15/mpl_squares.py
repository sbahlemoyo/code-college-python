#brings matplotlib plotting toolkit and use the alias plt to save typing time
import matplotlib.pyplot as plt

#this is our data that we will use to plot the graph
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#fig is the whole picture frame and ax is the canvas inside where you draw one specific plot, even if you have one plot at first this setup gives full control when wanting to scale and infuse multiple plots
fig, ax = plt.subplots()

#this draws the line, since only one list was passed it assumes that:
#the x values are the index positions [0, 1, 2, 3, 4]
#y-values are the square numbers so it'll plot (0, 1), (1, 4), (2, 9), (3, 16), (4, 25)
ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axes
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels
ax.tick_params(labelsize=14)
#it pops up a window with your beautiful line graph
plt.show()