import sys

def top_percent(numbers, percent):
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    
    # Compute the sum of all numbers
    total_sum = sum(sorted_numbers)
    print(f"Sum of all numbers: {total_sum}")
    
    # Calculate the threshold value (specified percentage of the sum)
    threshold = (percent / 100) * total_sum
    print(f"Cutoff threshold: {threshold}")
    
    # Iterate through the sorted list and keep adding numbers
    # until the sum exceeds or equals the threshold
    current_sum = 0
    top_numbers = []
    for num in sorted_numbers:
        current_sum += num
        top_numbers.append(num)
        if current_sum >= threshold:
            print(f"Stopping at {current_sum} because we reached or exceeded threshold {threshold}.  Difference: {current_sum-threshold}")
            print(f"Target percentage: {percent}")
            print(f"Actual percentage: {100*current_sum/total_sum}")
            break
    print(f"Keeping {len(top_numbers)} out of the original {len(numbers)} numbers ({100*len(top_numbers)/len(numbers)}%)")
    return top_numbers

# Function to read numbers from a file
def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(float(line.strip()))  # Assuming numbers are floats, adjust if necessary
    return numbers

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <percentage>")
        sys.exit(1)

    filename = sys.argv[1]
    percent = float(sys.argv[2])
    
    numbers = read_numbers_from_file(filename)
    result = top_percent(numbers, percent)
    print(f"Numbers contributing to the top {percent}%:", result)
