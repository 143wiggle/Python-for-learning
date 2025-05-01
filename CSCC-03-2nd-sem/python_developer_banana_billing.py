while True:
    print("\n--- Python Developer Transaction with Discount Process ---")

    banana_fruit_charge = float(input("Enter the total banana fruit charge (before discount): "))
    discount_rate = float(input("Enter the discount rate (e.g., 0.2 for 20%): "))
    
    discount_amount = banana_fruit_charge * discount_rate
    discounted_total = banana_fruit_charge - discount_amount

    print(f"Discount applied: ₱{discount_amount:.2f}")
    print(f"Total amount due after discount: ₱{discounted_total:.2f}")

    payment = float(input("Enter the Python developer's payment amount: "))
    balance = discounted_total - payment

    if balance > 0:
        print(f"Remaining balance: ₱{balance:.2f}")
    elif balance < 0:
        print(f"Change to be returned: ₱{abs(balance):.2f}")
    else:
        print("Payment complete. No remaining balance.")

    repeat = input("Do you want to assist another Python developer with a banana fruit billing transaction? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Thanks for using the Python Developer Transaction System. See you next time!")
        break
