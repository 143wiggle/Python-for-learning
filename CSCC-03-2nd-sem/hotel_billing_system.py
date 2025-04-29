# =====================================================
# CSCC03 - Programming Fundamentals
# Hotel Discount Billing System
# Author: Brent Frias Belmonte
# Description:
#     This Python program simulates a hotel billing system
#     that calculates discounts and processes payments.
#     It allows the user to:
#       - Input room charges
#       - Apply a discount
#       - Accept a payment
#       - Display the remaining balance or change
#       - Repeat the process for multiple guests
# =====================================================

while True:
    print("\nThank you for choosing our hotel!")
    print("--- Hotel Billing Transaction ---")

    # Step 1: Input room charge and discount rate
    room_charge = float(input("Enter the total room charge (before discount): "))
    discount_rate = float(input("Enter the discount rate (e.g., 0.2 for 20%): "))
    
    discount_amount = room_charge * discount_rate
    discounted_total = room_charge - discount_amount

    print(f"Discount applied: ₱{discount_amount:.2f}")
    print(f"Total amount due after discount: ₱{discounted_total:.2f}")

    # Step 2: Process guest payment
    payment = float(input("Enter the guest's payment amount: "))
    balance = discounted_total - payment

    # Step 3: Display remaining balance or change
    if balance > 0:
        print(f"Remaining balance: ₱{balance:.2f}")
    elif balance < 0:
        print(f"Change to be returned: ₱{abs(balance):.2f}")
    else:
        print("Payment complete. No remaining balance.")

    # Step 4: Ask if another guest will be billed
    repeat = input("Would you like to process another guest? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Thank you for using the Hotel Billing System. Have a great day!")
        break
