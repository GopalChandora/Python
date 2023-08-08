import matplotlib.pyplot as plt
import numpy as n

x = n.array([1,4])
y = n.array([2,3])
 
#plt.plot(x,y) #line will appear

#plt.plot(x,y,'o') # only pionts will be seen

#plt.plot(x,y, marker='D', ms = 20,mfc= 'red',mec='yellow')# color to face edge 

#plt.plot(x, y, linestyle='dotted') # we can change linestyle(ls) as dotted ,dashed,solid,dashed.dot etc

#plt.plot(x, y, color ='yellow') # we can give color to line by giving (yellow or jusy y )

#plt.plot(x, y, linewidth=3) # we can change width of line by writing( linewidth or just lw)

plt.title(' Straight Line ', loc = 'left') # provide title to the graph and loc used for alignment of title

plt.xlabel('X-Axis')# provide label to x axis
plt.ylabel('Y-Axis')# provide label to y axis

plt.grid(axis ='y') # provides grid line to graph by defualt grid is to both axis,if we give argument (axis = 'y') then it will grid y axis only 


plt.subplot(1,2,1)
plt.plot(x,y)


x = n.array([1,4,6])
y = n.array([2,5,3])

plt.plot(x,y)
plt.subplot(1,2,2)

plt.show() # it show the graph


