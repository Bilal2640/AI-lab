import statistics
import numpy as np

# Dataset validation
def validate_dataset(dataset):
    if not dataset or not all(isinstance(i, (int, float)) for i in dataset):
        raise ValueError("Dataset must be a non-empty list of numeric values.")

# Calculation of Mean, Median, Mode
def calculate_mean_median_mode(dataset):
    mean = statistics.mean(dataset)
    median = statistics.median(dataset)
    try:
        mode = statistics.mode(dataset)
    except statistics.StatisticsError:
        mode = 'No unique mode found'
    return mean, median, mode

# Calculation of Variance and Standard Deviation
def calculate_variance_std(dataset):
    variance = np.var(dataset, ddof=1) # ddof=1 for sample variance
    std_deviation = np.sqrt(variance)
    return variance, std_deviation

# Main function to run the program
def main():
    # Example dataset
    dataset = [12, 15, 12, 18, 19, 19, 19, 21, 22, 20, 25, 28, 25]
    try:
        validate_dataset(dataset)
        mean, median, mode = calculate_mean_median_mode(dataset)
        variance, std_deviation = calculate_variance_std(dataset)
        print(f"Mean: {mean}\n Median: {median}\n Mode: {mode}")
        print(f"Variance: {variance}\n Standard Deviation: {std_deviation}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
