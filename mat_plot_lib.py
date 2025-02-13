# Line Plot
import matplotlib.pyplot as plt  
# Sample data  
x = [1, 2, 3, 4, 5]  
y = [10, 20, 25, 30, 40]  
# Create a line plot  
plt.plot(x, y, marker="o", linestyle="--", color="red", label="Growth")  
# Labels and title  
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Simple Line Plot")  
plt.legend()  # Show legend  
# Show the plot  
plt.show()

# Scatter Plot
import matplotlib.pyplot as plt  
# Sample data  
x = [1, 2, 3, 4, 5]  
y = [10, 20, 25, 30, 40]  
# Create scatter plot  
plt.scatter(x, y, color="blue", marker="s")  
# Labels and title  
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.title("Scatter Plot Example")  
# Show the plot  
plt.show()


# Histogram
import matplotlib.pyplot as plt  
import numpy as np  
# Generate random data  
data = np.random.randn(1000)  
# Create histogram  
plt.hist(data, bins=30, color="green", edgecolor="black")  
# Labels and title  
plt.xlabel("Values")  
plt.ylabel("Frequency")  
plt.title("Histogram Example")  
# Show the plot  
plt.show()


# Pie Chart
import matplotlib.pyplot as plt  
# Sample data  
labels = ["Apple", "Banana", "Cherry", "Dates"]  
sizes = [20, 35, 30, 15]  
# Create pie chart  
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["red", "yellow", "pink", "brown"])  
# Title  
plt.title("Fruit Distribution")  
# Show the plot  
plt.show()


# SubPlots
import matplotlib.pyplot as plt  
import numpy as np  
# Sample data  
x = np.linspace(0, 10, 100)  
y1 = np.sin(x)  
y2 = np.cos(x)  
# Create subplots  
fig, ax = plt.subplots(2, 1, figsize=(8, 6))  
# First subplot  
ax[0].plot(x, y1, color="blue")  
ax[0].set_title("Sine Wave")  
# Second subplot  
ax[1].plot(x, y2, color="red")  
ax[1].set_title("Cosine Wave")  
# Adjust layout  
plt.tight_layout()  
# Show the plot  
plt.show()


# Customizing Grid, Labels, and Ticks
import matplotlib.pyplot as plt  
# Sample data  
x = [1, 2, 3, 4, 5]  
y = [10, 20, 30, 40, 50]  
# Create line plot  
plt.plot(x, y, marker="o", linestyle="-", color="purple")  
# Customizing grid  
plt.grid(True, linestyle="--", linewidth=0.5)  
# Customizing ticks  
plt.xticks([1, 2, 3, 4, 5], ["A", "B", "C", "D", "E"])  
# Labels and title  
plt.xlabel("Categories")  
plt.ylabel("Values")  
plt.title("Custom Grid and Ticks")  
# Show the plot  
plt.show()


