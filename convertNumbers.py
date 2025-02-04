import time


def process_file(filepath):
    try:
        with open(filepath, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return

    results = []
    for num in numbers:
        binary = decimal_to_binary(num)
        hexadecimal = decimal_to_hexadecimal(num)
        result_str = f"Decimal: {num}, Binary: {binary}, Hexadecimal: {hexadecimal}"
        results.append(result_str)
    return results


def decimal_to_binary(decimal_num):
    """Converts a decimal number to its binary representation."""
    if decimal_num == 0:
        return "0"

    binary_representation = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_representation = str(remainder) + binary_representation
        decimal_num //= 2
    return binary_representation


def decimal_to_hexadecimal(decimal_num):
    """Converts a decimal number to its hexadecimal representation."""
    if decimal_num == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hex_representation = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_representation = hex_chars[remainder] + hex_representation
        decimal_num //= 16
    return hex_representation


def main():
    # Get file path from user input
    filepath = input("Enter the file path: ")
    start_time = time.time()
    # Process the file and print results
    conversion_results = process_file(filepath)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

    # Print to the console
    for result in conversion_results:
        print(result)

    # Write to the file
    with open("ConvertionResults.txt", "w") as file:
        for result in conversion_results:
            file.write(result + "\n")


if __name__ == "__main__":
    main()
