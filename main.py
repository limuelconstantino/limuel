import circle_calculator

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circle_calculator.calculate_area(radius)
    circumference = circle_calculator.calculate_circumference(radius)

    print(f"Radius: {radius}")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")

if __name__ == "__main__":
    main()
