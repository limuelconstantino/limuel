import math

def input_radius():
    radius = float(input("Please enter the radius of the circle: "))
    return radius

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def display_results(area, circumference):
    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")

def main():
    radius = input_radius()
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    display_results(area, circumference)

if __name__ == "__main__":
    main()