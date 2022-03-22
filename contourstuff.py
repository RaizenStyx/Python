from matplotlib import pyplot as plt


x_value = [1, 2, 3, 4]
y_value = [5, 4, 6, 2]

plt.scatter(x_value, y_value)

other_x_val = [1, 2, 3, 4]
other_y_val = [4, 2, 3, 9]

plt.plot(other_x_val, other_y_val, color="navy")
plt.title("Example")

plt.xlabel("x val")
plt.ylabel("y val")


plt.show()