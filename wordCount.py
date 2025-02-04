import time
import sys
import re


def count_word_freq(filepath):
    """
    Counts the frequency of distinct words in a file.

    Args:
        filepath: The path to the input file.

    Returns:
        A dictionary where keys are distinct words and values are their frequencies.
        Returns an empty dictionary if the file does not exist or cannot be opened.
    """

    word_frequencies = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    if word in word_frequencies:
                        word_frequencies[word] += 1
                    else:
                        word_frequencies[word] = 1
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return word_frequencies


def main():
    # Get file path from user input
    filepath = input("Enter the file path: ")
    start_time = time.time()
    # Process the file and print results
    data = count_word_freq(filepath)

    if data:  # Check if word_frequencies is not empty
        print("Word Frequencies:")
        for word, frequency in data.items():
            print(f"{word}: {frequency}")

        try:
            with open("WordCountResults.txt", "w", encoding='utf-8') as outfile:
                outfile.write("Word Frequencies:\n")
                for word, frequency in data.items():
                    outfile.write(f"{word}: {frequency}\n")
            print("Results saved to WordCountResults.txt")

        except Exception as e:
            print(f"Error writing to file: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)


if __name__ == "__main__":
    main()
