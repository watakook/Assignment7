import sys
import json

def validate_numbers(numbers):
    """ Validate input to ensure it contains only integers """
    try:
        return [int(num) for num in numbers.split(",")]
    except ValueError:
        return None

def bitwise_operations(numbers):
    """ Perform AND, OR, XOR bitwise operations """
    and_result = numbers[0]
    or_result = numbers[0]
    xor_result = numbers[0]

    for num in numbers[1:]:
        and_result &= num
        or_result |= num
        xor_result ^= num

    return and_result, or_result, xor_result

def filter_numbers(numbers, threshold):
    """ Filter numbers greater than the threshold value """
    return [num for num in numbers if num > threshold]

def main():
    # Retrieve arguments from PHP
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing arguments"}))
        return
    
    numbers_str = sys.argv[1]
    threshold_str = sys.argv[2]

    numbers = validate_numbers(numbers_str)
    if numbers is None:
        print(json.dumps({"error": "Invalid input"}))
        return

    try:
        threshold = int(threshold_str)
    except ValueError:
        print(json.dumps({"error": "Threshold must be an integer"}))
        return

    # Perform bitwise operations
    and_result, or_result, xor_result = bitwise_operations(numbers)

    # Filter numbers
    filtered_numbers = filter_numbers(numbers, threshold)

    # Output results in JSON format
    result = {
        "AND": and_result,
        "OR": or_result,
        "XOR": xor_result,
        "Filtered": filtered_numbers
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
