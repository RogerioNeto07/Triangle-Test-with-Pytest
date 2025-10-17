def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def main():
    side_1 = int(input("Enter side 1: "))
    side_2 = int(input("Enter side 2: "))
    side_3 = int(input("Enter side 3: "))

    if is_triangle(side_1, side_2, side_3):
        print("This is a triangle.")
    else:
        print("This is not a triangle.")

if __name__ == "__main__":
    main()
