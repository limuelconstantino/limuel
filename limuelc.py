def get_length():
    return float(input("Enter the length of the rectangle: "))

def get_width():
    return float(input("Enter the width of the rectangle: "))

def calculate_area(length, width):
    return length * width

def main():
    length = get_length()
    width = get_width()
    area = calculate_area(length, width)
    print(f"The area of the rectangle is {area} square units.")

if __name__ == "__main__":
    main()