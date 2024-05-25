def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            return None  # Invalid binary digit
    
        power -= 1
    
    return decimal

def main():
    binary = input("Enter a binary number: ")
    
    decimal = binary_to_decimal(binary)
    if decimal is not None:
        print(f"The binary number: {binary} <==> the decimal number {decimal}.")
    else:
        print("Error. Please check the input.")

if __name__ == "__main__":
    main()

