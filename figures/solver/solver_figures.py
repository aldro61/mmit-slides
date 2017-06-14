"""


"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set_style("white")

x = np.linspace(-1, 1, 100000)

plt.clf()
breakpoints = np.random.uniform(-1, 1, 100)
signs = np.random.randint(0, 2, 100)
signs[signs == 0] = -1

f_x = np.zeros(len(x))
for b, s in zip(breakpoints, signs):
    contrib = s * (x - b)
    contrib[contrib <= 0] = 0
    f_x += contrib

f_breakpoints = np.zeros(len(breakpoints))
for b, s in zip(breakpoints, signs):
    contrib = s * (breakpoints - b)
    contrib[contrib <= 0] = 0
    f_breakpoints += contrib

plt.scatter(breakpoints, f_breakpoints, color="red", s=40)
plt.plot(x, f_x, color="black")
#plt.arrow(0, 0.5, 0, -0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')

plt.xlabel(r"$\mu$", fontsize=16)
plt.ylabel("Cost", fontsize=16)

plt.show()