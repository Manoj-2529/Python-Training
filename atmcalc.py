pin = int(input())
acc_bal = 0

if pin == 9542:
    print("Welcome to State Bank of India Where Bank antene Oka temple")

    while True:
        print("1.Deposit")
        print("2.Withdrawl")
        print("3.Balance Enquiry")
        print("4.Exit")

        choice = int(input("Enter your choice: "))

        if (choice == 1):
            amount = int(input("Enter amount to deposit: "))
            acc_bal = acc_bal + amount
            print("Amount deposited:", amount)

        elif (choice == 2):
            amount = int(input("Enter withdrawal amount: "))
            if (amount <= acc_bal):
                acc_bal = acc_bal -  amount
                print("Money debited:", amount)
            else:
                print("Acc lo dabbulu levu ra ayya!")

        elif (choice == 3):
            print("Current Balance:", acc_bal)

        elif (choice == 4):
            print("Bank nunchi bayataku vellu ra babu!")
            break

        else:
            print("Invalid choice")
            break

else:
    print("Pin chusko ra!")