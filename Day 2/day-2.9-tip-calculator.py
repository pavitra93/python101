# Welcome message 
print("Welcome to tip calculator!\n")

# Get total bill amount 
bill_amount = float(input("Get total bill amount\n"))

# Get tip percent
tip_percent = int(input("Enter tip percent 5,10 or 12\n"))

# Get total number of persons to split
total_person = int(input("How many people to split the bill?\n"))


bill_amount += bill_amount *  (tip_percent / 100) 
per_person_bill = bill_amount / total_person
per_person_bill_round = round(per_person_bill,2)


print(f"Each per will pay {per_person_bill_round} amount.")