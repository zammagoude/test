print("hello world")

#Without walrus operator
n = 0
while n < 10:
    print(n)
    n += 1

# With walrus operator
n = -1
while (n := n + 1) < 10:
    print(n)

print("\n")


# # Without walrus operator
squares = []
for x in range(10):
    squares.append(x * x)

# print(squares)

# # With walrus operator
# squares = [x * x for x in range(10)]
# print(squares)

# # Another example
# squares = [y * y for x in range(10) if (y := x * x) < 25]
# print(squares)

#help(lis
planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)