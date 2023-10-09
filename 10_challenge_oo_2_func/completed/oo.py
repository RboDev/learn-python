from math import pi


def rectangle_area(width: float, height: float) -> float:
    return width * height


def rectangle_perimeter(width: float, height: float) -> float:
    return 2 * (width + height)


def circle_area(radius: float) -> float:
    return pi * radius**2


def circle_perimeter(radius: float) -> float:
    return 2 * pi * radius


def main() -> None:

    rectangle = (4, 5)
    square = (3, 3)
    circle = 2

    total_area = sum([
        rectangle_area(*rectangle),
        rectangle_area(*square),
        circle_area(circle)
    ])
    
    total_perimeter = sum([
        rectangle_perimeter(*rectangle),
        rectangle_perimeter(*square),
        circle_perimeter(circle)
    ])


    print("Total Area:", total_area)
    print("Total Perimeter:", total_perimeter)


if __name__ == "__main__":
    main()