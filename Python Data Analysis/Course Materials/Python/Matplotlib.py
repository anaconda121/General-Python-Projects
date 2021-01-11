 #control b to show build output and graph


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000) #generates an array of 1000 numbers between 0 and 10

#formatting graph to make it more professional
plt.rcParams.update({'font.size' : 15}) #changinig font-size to 15px
plt.plot(x, np.sin(x), color = "black", linestyle = "dotted", label = "sin(x)" ) #random nums act as x-cor, sin(x) value at those x-cor = y-cor
plt.title("Graph of Sin(x)")
plt.axis([0, 10, -1.05, 1.05]) #first 2 are x-axs, second 2 are y-axis
plt.legend(loc = "lower left")
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.show()

y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

# lines is a list of plt.Line2D instances
print(plt.legend(lines[:2], ['first', 'second']))

#creating graph that shows error levels and certainity
xCoord = np.linspace(0, 10, 50)
unsurePercent = 0.2

yCoord = np.sin(xCoord) + unsurePercent * np.random.randn(50) #generates noisy sin curve b/c of unsure% times random num
plt.errorbar(xCoord, yCoord, yerr = unsurePercent, fmt = ".k", ecolor= 'green', elinewidth = 3, capsize = 5); 
plt.show()

"""
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range, plt.errorbar(xCoord, yCoord, yerr = unsurePercent, fmt = ".k", ecolor= 'green', elinewidth = 3, capsize = 5); 
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range
"""

fig = plt.figure(figsize = (12, 12))
x = np.linspace(0, 10, 1000) 
y = np.sin(x)

for i in range (6):
    fig.add_subplot(3, 2, i+1) #fig.add_subplot creates set of graphs next to each other, first digit is the number of rows, the second the number of columns, and the third the index of the subplot.
    plt.style.use(plt.style.available[i]) #prints graph in style in rotation
    plt.plot(x, y)
    
    plt.text(s = plt.style.available[i], x = 2, y = 1, color = 'red')


#multiple graphs
# Change default font size
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
ax = plt.axes()
plt.show()

# Solid line, color specified by its name
plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='blue')
plt.show()
# Short name for color, dashed line
plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='vert')
plt.show()
# Grayscale between 0 and 1, dashes and dots
plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='gris')
plt.show()
# RGB color, dotted line
plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='rouge')
plt.show()
# Axis limits. Try also 'tight' and 'equal' to see their effect
plt.axis([-1, 11, -1.5, 1.5]);

# Labels
plt.title("Example of a graph")

# The legend is generated from the argument 'label' of 'plot'
# 'loc' specified the placement of the legend.
plt.legend(loc='lower left');

# Axis titles
ax = ax.set(xlabel='x', ylabel='sin(x)')

#bar graph
x = np.random.randn(1000)

plt.style.use('classic')
fig=plt.figure(figsize=(5,3))
ax = plt.axes(facecolor='#E6E6E6')
# Display ticks underneath the axis
ax.set_axisbelow(True)
# White frame
plt.grid(color='w', linestyle='solid')

# Hide the frame
for spine in ax.spines.values():    
    spine.set_visible(False)
    
# Hide the markers at the top and the right
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# We can personalise the markers, and rotate them
marqueurs = [-3, -2, -1, 0, 1, 2, 3]
xtick_labels = ['A', 'B', 'C', 'D', 'E', 'F']
plt.xticks(marqueurs, xtick_labels, rotation=30)

# Change the color of markers
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():    
    tick.set_color('gray')
for tick in ax.get_yticklabels():    
    tick.set_color('gray')    
    
# Change the color of the edges
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');
plt.show()







"""
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range, plt.errorbar(xCoord, yCoord, yerr = unsurePercent, fmt = ".k", ecolor= 'green', elinewidth = 3, capsize = 5); 
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range
"""

fig = plt.figure(figsize = (12, 12))
x = np.linspace(0, 10, 1000) 
y = np.sin(x)

for i in range (6):
    fig.add_subplot(3, 2, i+1) #fig.add_subplot creates set of graphs next to each other, first digit is the number of rows, the second the number of columns, and the third the index of the subplot.
    plt.style.use(plt.style.available[i]) #prints graph in style in rotation
    plt.plot(x, y)
    
    plt.text(s = plt.style.available[i], x = 2, y = 1, color = 'red')


#multiple graphs
# Change default font size
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
ax = plt.axes()
plt.show()

# Solid line, color specified by its name
plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='blue')
plt.show()
# Short name for color, dashed line
plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='vert')
plt.show()
# Grayscale between 0 and 1, dashes and dots
plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='gris')
plt.show()
# RGB color, dotted line
plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='rouge')
plt.show()
# Axis limits. Try also 'tight' and 'equal' to see their effect
plt.axis([-1, 11, -1.5, 1.5]);

# Labels
plt.title("Example of a graph")

# The legend is generated from the argument 'label' of 'plot'
# 'loc' specified the placement of the legend.
plt.legend(loc='lower left');

# Axis titles
ax = ax.set(xlabel='x', ylabel='sin(x)')

#bar graph
x = np.random.randn(1000)

plt.style.use('classic')
fig=plt.figure(figsize=(5,3))
ax = plt.axes(facecolor='#E6E6E6')
# Display ticks underneath the axis
ax.set_axisbelow(True)
# White frame
plt.grid(color='w', linestyle='solid')

# Hide the frame
for spine in ax.spines.values():    
    spine.set_visible(False)
    
# Hide the markers at the top and the right
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# We can personalise the markers, and rotate them
marqueurs = [-3, -2, -1, 0, 1, 2, 3]
xtick_labels = ['A', 'B', 'C', 'D', 'E', 'F']
plt.xticks(marqueurs, xtick_labels, rotation=30)

# Change the color of markers
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():    
    tick.set_color('gray')
for tick in ax.get_yticklabels():    
    tick.set_color('gray')    
    
# Change the color of the edges
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');
plt.show()