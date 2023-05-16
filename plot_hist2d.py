import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('points.csv')

# Set up the plot
plt.figure(figsize=(10, 6))
plt.title('Histogram of Point Cloud')
plt.xlabel('x')
plt.ylabel('y')

plt.xlim(0, 1280)
plt.ylim(720, 0)  # Invert the y-axis

# Plot the histogram
plt.hist2d(df['x'], df['y'], bins=(32, 18), cmap=plt.cm.jet)

# Add a colorbar for reference
plt.colorbar()

# Invert the y-axis
plt.gca().invert_yaxis()

# Display the plot
plt.show()