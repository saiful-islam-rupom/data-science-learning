import numpy as np
import matplotlib.pyplot as plt
############### plotting a 2D graph ###########
#-------- x=y ------------
# x = np.linspace(-10,10,100) # np.linspace - equal distance numbers (first,last, how much points)
# print(x)

# y = x
# print(y)

# plt.plot(x,y) # plt.plot() - to create graph
# plt.show()    # plt.show() - to show graph

#----------another example--- y = x^2

# x = np.linspace(-10,10,100)
# y = x**2

# plt.plot(x,y)
# plt.show()

# another example ------ y = sin(x)

# x = np.linspace(-10,10,100)
# y = np.sin(x)

# plt.plot(x,y)
# plt.show()

# another example ---- y = xlog(x)

# x = np.linspace(-10,10,100)
# y = x*(np.log(x))

# plt.plot(x,y)
# plt.show()

#anothe example -------- sigmoid-----

# x = np.linspace(-10,10,100)
# y = 1/(1+(np.exp(-(x))))

# plt.plot(x,y)
# plt.show()
