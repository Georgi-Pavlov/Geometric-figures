import figures

figure_types = ["circle", "triangle", "rectangle", "pentagon", "hexagon", "octagon"]
while True:
    figure = input("Please select the figure type [circle, triangle, rectangle, "
                   "pentagon, hexagon, octagon]: ").lower()

    if figure in figure_types:
        break
    else:
        print("Invalid selection. Please try again.")

if figure == "triangle":
    while True:
        sides = []
        for _ in range(3):
            try:
                side = float(input("Please enter the side length of the triangle: "))
                sides.append(side)
            except ValueError:
                print("Invalid input. Please try again.")
                break

        try:
            figure = figures.Triangle(sides[0], sides[1], sides[2])
        except ValueError as e:
            print("Error:", e)
        else:
            print(f"The figure is a {figure.type_()} triangle with perimeter: {figure.perimeter()} and area: {figure.area()}")
            break
