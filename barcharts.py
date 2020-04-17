import matplotlib.pyplot as plt

plt.bar([1,3,5,9,7],[10,12,13,11,12], label='Example One')
plt.bar([2, 4, 6, 8 ,10], [9, 11, 8, 7, 10], label='Example Two',color='g')
plt.legend()
plt.xlabel('Bar Label')
plt.ylabel('Bar Height')
plt.title("Epic Graph")
plt.show()