import numpy as np
import matplotlib.pyplot as plt

# Step 2: Dataset Selection - Generate synthetic data
np.random.seed(0)
X = 2.5 * np.random.randn(100) + 1.5   # Array of 100 values with mean = 1.5, stddev = 2.5
res = 0.5 * np.random.randn(100)       # Generate 100 residual terms
y = 2 + 0.3 * X + res                  # Actual values of Y

# Step 3: Data Exploration - Plot a scatter plot of the synthetic dataset
plt.scatter(X, y)
plt.xlabel('Independent Variable X')
plt.ylabel('Dependent Variable Y')
plt.title('Scatter Plot of Independent vs. Dependent Variable')
plt.show()

# Step 4: Implementation of Simple Linear Regression - Calculate slope and intercept
x_mean = np.mean(X)
y_mean = np.mean(y)
Xy = np.sum(y*X) - len(X)*y_mean*x_mean
Xx = np.sum(X*X) - len(X)*x_mean*x_mean
b1 = Xy / Xx
b0 = y_mean - (b1 * x_mean)

# Step 6: Prediction - Use the model to predict Y given X
y_pred = b0 + b1 * X

# Step 7: Plotting the Regression Line - Plot the regression line with the scatter plot
plt.scatter(X, y, label='Data points')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Independent Variable X')
plt.ylabel('Dependent Variable Y')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()
