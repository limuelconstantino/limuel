def get_length():
    return float(input("Enter the length of the triangle: "))

def get_width():
    return float(input("Enter the width of the triangle: "))

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def main():
    length = get_length()
    width = get_width()
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"The area of the rectangle is {area} square units.")
    print(f"The perimeter of the Triangle is {perimeter} units.")
    
if __name__ == "__main__":
    main()