import matplotlib.pyplot as plt

addition = [0.49563, 0.50770, 0.42316, 0.37580]

fulllex = [0.00761, 0.05631, 0.18877, 0.22559]

matrix = [0.00791, 0.05828, 0.19035, 0.23046]

trans_weight = [0.00751, 0.05682, 0.18364, 0.21365]

plt.plot(addition, label='addition', color='g', linestyle='-')
plt.plot(fulllex, label='fulllex', color='y', linestyle='-')
plt.plot(matrix, label='matrix', color='r', linestyle='-')
plt.plot(trans_weight, label='trans_weight', color='b', linestyle='-')

plt.xticks([0, 1, 2, 3], ['1%', '5%', '25%', '50%'])
plt.ylabel('Dev Loss')
plt.legend(fontsize='xx-small', loc='right', bbox_to_anchor=(1, 0.3))
plt.show()
# plt.savefig('model.png')