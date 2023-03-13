import matplotlib.pyplot as plt

x = [2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 2, 8, 3, 7, 4, 6, 5]

plt.plot(x, y, color = 'green')
plt.scatter(x, y, color = 'red')
plt.title('Evolução das vendas')
plt.xlabel('tempo')
plt.ylabel('vendas')
plt.legend(['previsão', 'verificado'])
plt.grid()

plt.show()