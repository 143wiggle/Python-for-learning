while True:
    print("\n--- Sample Transaction with Discount Process ---")

    banana_fruit_charge = float(input("Enter the total banana fruit charge (before discount): "))
    discount_rate = float(input("Enter the discount rate (e.g., 0.2 for 20%): "))
    
    discount_amount = banana_fruit_charge * discount_rate
    discounted_total = banana_fruit_charge - discount_amount

    print(f"Discounted price of {banana_fruit_charge} is : ₱{discount_amount:.2f}")
    print(f"Total amount due after discount: ₱{discounted_total:.2f}")

    payment = float(input("Enter the payment amount: "))
    balance = discounted_total - payment

    if balance > 0:
        print(f"Remaining balance: ₱{balance:.2f}")
    elif balance < 0:
        print(f"Change to be returned: ₱{abs(balance):.2f}")
    else:
        print("Payment complete. No remaining balance.")

    repeat = input("Do you want to assist another polite student with a banana fruit billing transaction? (Y/N): ").strip().lower()
    if repeat != 'y':
        print("Thanks for using the Sample Transaction System. See you next time!")
        break
