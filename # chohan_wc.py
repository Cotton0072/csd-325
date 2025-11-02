# chohan_wc.py
# Modified by Will Cotton
# -----------------------------------------------------
# Changes Made:
# 1. Input prompt changed to "WC:" instead of the default prompt.
# 2. House percentage increased from 10% to 12%.
# 3. Added a notice in the introduction about the 10 mon bonus for rolling a 2 or 7.
# 4. Added logic that awards a 10 mon bonus if the dice total equals 2 or 7.
# 5. Commented code for clarity and maintainability.
# -----------------------------------------------------

import random

# --- Game Introduction ---
print("Welcome to the game of Cho-Han!")
print("You start with 100 mon.")
print("Note: If you roll a total of 2 or 7, you get a 10 mon bonus!")  # Added new rule notice

# --- Starting purse ---
purse = 100

# --- Main game loop ---
while True:
    print(f"\nYou currently have {purse} mon.")

    # Changed input prompt to initials
    bet = int(input("WC: "))  # <-- Changed here

    # Exit condition
    if bet == 0:
        print("Thanks for playing! Come back soon.")
        break

    # Check for invalid bet
    if bet > purse:
        print("You don't have enough mon to make that bet.")
        continue

    # Roll two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2

    # --- Bonus Rule for rolling 2 or 7 ---
    if dice_total == 2 or dice_total == 7:
        print(f"You rolled a total of {dice_total}! You get a 10 mon bonus!")  # Message for bonus
        purse += 10  # Add 10 mon bonus to purse

    # Ask player to guess Cho (even) or Han (odd)
    choice = input("Cho (even) or Han (odd)? ").lower()

    # Determine if total is even or odd
    result = "cho" if dice_total % 2 == 0 else "han"

    print(f"The dice show {dice1} and {dice2} (total: {dice_total}), which is {result}.")

    # Determine win or lose
    if choice == result:
        print("You win!")
        purse += bet
    else:
        print("You lose!")
        purse -= bet

    # --- House percentage cut changed from 10% to 12% ---
    house_cut = int(purse * 0.12)
    purse -= house_cut
    print(f"The house takes 12%, which is {house_cut} mon.")

    # Check if player ran out of money
    if purse <= 0:
        print("You're out of mon! Game over.")
        break

# --- End of program ---
print("Game session ended. Final purse:", purse)
