def get_starting_number():
    while True:
        try:
            bottles = int(input("How many bottles of bear on the wall?"))
            if bottles >= 1:
                return bottles
            else:
                print("Please enter a number 1 or a number greater than one")
        except ValueError:
            print("Please enter a valid number of bottles! ")
    


def sing(starting_bottles):
    for bottles in range(starting_bottles, 0, -1):
        if bottles > 2:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles-1} bottles of beer on the wall.\n")
        elif bottles == 2:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles-1} bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!")




