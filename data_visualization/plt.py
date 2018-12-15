import matplotlib.pyplot as plt
x = list(range(1,100))
y = [a*a for a in x]
plt.scatter(x, y, s=30, edgecolor = 'none', c=y, cmap = plt.cm.Greens)
plt.title(r'y = x^2')
plt.savefig('abc', bbox_inches = 'tight')