"""


"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

plt.clf()

plt.gcf().set_size_inches(5, 1)

plt.plot([0, 1], [0, 0], linestyle="--", color="grey", linewidth=2)
plt.scatter([0], [0], edgecolor="black", linewidth=1, facecolor="white", s=70, zorder=100)
plt.text(0, 0.13, r"$\underline{y}$", fontsize=18)
plt.scatter([1], [0], edgecolor="black", linewidth=1, facecolor="black", s=70, zorder=100)
plt.text(0.97, 0.18, r"$\overline{y}$", fontsize=18)

# Plot left tail
x = np.linspace(-1, 0)
plt.plot(x, x**2, color="red", linewidth=2)

# Plot right tail
x = np.linspace(1, 2)
plt.plot(x, (1.0 - x)**2, color="red", linewidth=2)


plt.ylim(ymax=0.8)
plt.ylabel(r"Cost")

plt.xlabel(r"$\mu$")
plt.savefig("interval_loss.pdf", bbox_inches="tight")

plt.xlabel(r"$f(\mathbf{x})$")
plt.savefig("interval_loss_fx.pdf", bbox_inches="tight")
