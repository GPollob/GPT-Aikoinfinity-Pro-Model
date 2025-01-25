import matplotlib.pyplot as plt

# Example data: Model accuracies over iterations
iterations = [1, 2, 3, 4, 5]
accuracies = [78, 85, 89, 92, 95]

plt.plot(iterations, accuracies, marker='o')
plt.title("Model Accuracy Over Iterations")
plt.xlabel("Iterations")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.show()
