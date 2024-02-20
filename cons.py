import math

def input_radius():
    while True:
        try:
            radius = float(input("Please enter the radius of the circle: "))
            return radius
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def calculate_diameter(radius):
    diameter = 2 * radius
    return diameter

def display_results(area, circumference, diameter):
    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")
    print(f"The diameter of the circle is: {diameter}")

def main():
    radius = input_radius()
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    diameter = calculate_diameter(radius)
    display_results(area, circumference, diameter)

if __name__ == "__main__":
    main()