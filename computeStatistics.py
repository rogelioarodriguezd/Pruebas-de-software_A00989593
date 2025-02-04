import time
import math


def process_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []  # Return an empty list to indicate failure

    data = []
    for i, line in enumerate(lines):
        try:
            num = float(line.strip())  # Convert each line to a number
            data.append(num)
        except ValueError:
            print(f"Error: Invalid data on line {i+1}: '{line.strip()}'")

    return data


def calculate_std_dev(data):
    n = len(data)
    if n == 0:
        return 0  # Handle empty dataset

    # Calculate the mean
    sum_of_values = sum(data)
    mean = sum_of_values / n

    # Calculate the squared differences from the mean
    squared_differences = [(x - mean) ** 2 for x in data]

    # Calculate the variance
    variance = sum(squared_differences) / n

    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)

    return standard_deviation


def calculate_median(data):
    """Calculates the median of a list of numbers."""
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_data[n // 2]
    return median


def calculate_mean(data):
    """Calculates the mean of a list of numbers."""
    total = sum(data)
    return total / len(data) if len(data) > 0 else 0


def calculate_variance(data, mean):
    """Calculates the variance of a list of numbers."""
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data) if len(data) > 0 else 0
    return variance


def calculate_mode(data):
    """Calculates the mode of a list of numbers."""
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    max_count = 0
    mode = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode = num
    return mode


def main():
    # Get file path from user input
    filepath = input("Enter the file path: ")
    start_time = time.time()
    # Process the file and print results
    data = process_file(filepath)

    if data:
        print("Numbers extracted from the file")

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = f"""

Time elapsed: {elapsed_time:.4f} seconds

Statistics:

Mean: {mean}
Median: {median}
Mode: {mode}
Variance: {variance}
Standard Deviation: {std_dev}

    """

    print(results)

    with open("StatisticsResults.txt", "w") as outfile:
        outfile.write(results)


if __name__ == "__main__":
    main()
