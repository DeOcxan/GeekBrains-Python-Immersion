def check_triangle_existence(a: float, b: float, c: float) -> bool:
    """
    Checks if a triangle can exist with the given side lengths.
    A triangle exists only if the sum of any two of its sides is greater than the third side.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)

def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Determines if the triangle is equilateral, isosceles, or scalene.
    Assumes the sides can form a valid triangle.
    """
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def main():
    """
    Main function to get triangle side inputs and print results.
    """
    try:
        side_a = float(input("Enter length of side a: "))
        side_b = float(input("Enter length of side b: "))
        side_c = float(input("Enter length of side c: "))

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            print("Side lengths must be positive.")
            return

        if check_triangle_existence(side_a, side_b, side_c):
            triangle_type = get_triangle_type(side_a, side_b, side_c)
            print(f"A triangle can be formed with sides {side_a}, {side_b}, {side_c}.")
            print(f"The triangle is {triangle_type}.")
        else:
            print(f"A triangle cannot be formed with sides {side_a}, {side_b}, {side_c}.")
            if side_a >= side_b + side_c:
                print(f"Side a ({side_a}) is not less than the sum of side b ({side_b}) and side c ({side_c}).")
            if side_b >= side_a + side_c:
                print(f"Side b ({side_b}) is not less than the sum of side a ({side_a}) and side c ({side_c}).")
            if side_c >= side_a + side_b:
                print(f"Side c ({side_c}) is not less than the sum of side a ({side_a}) and side b ({side_b}).")

    except ValueError:
        print("Invalid input. Please enter numeric values for side lengths.")

if __name__ == "__main__":
    main() 