def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down, pass it around, no more bottles of beer on the wall.\n")

# Main program
try:
    start_count = int(input("How many bottles of beer are on the wall? "))
    if start_count < 1: 
        print("Please enter a number greater than 0.")
    else:
        countdown(start_count)
        print("Time to buy more beer!")
except ValueError:
    print("Invalid input. Please enter a whole number.")

