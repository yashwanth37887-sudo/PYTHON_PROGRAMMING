
# Hospital Billing and Patient Classification System

def hospital_billing():

    print("======================================")
    print(" HOSPITAL BILLING SYSTEM")
    print("======================================")

    # Patient details
    name = input("Enter Patient Name: ")

    try:
        age = int(input("Enter Patient Age: "))

        consultation = float(
            input("Enter Consultation Charges: ₹")
        )

        diagnostic = float(
            input("Enter Diagnostic Charges: ₹")
        )

        treatment = float(
            input("Enter Treatment Charges: ₹")
        )

        concession_card = input(
            "Does the patient have a concession card? (yes/no): "
        ).lower()

        # Validate inputs
        if age < 0:
            raise ValueError("Age cannot be negative.")

        if min(consultation, diagnostic, treatment) < 0:
            raise ValueError("Charges cannot be negative.")

        if concession_card not in ["yes", "no"]:
            raise ValueError("Enter yes or no.")

        # Calculate gross bill
        gross_bill = consultation + diagnostic + treatment

        # Calculate concessions
        senior_discount = 0
        card_discount = 0

        if age >= 60:
            senior_discount = consultation * 0.10

        if concession_card == "yes":
            card_discount = (diagnostic + treatment) * 0.20

        # Total concession
        total_discount = senior_discount + card_discount

        # Validate billing constraint
        if total_discount > gross_bill:
            total_discount = gross_bill

        # Final payable amount
        final_amount = gross_bill - total_discount

        # Patient classification
        if final_amount <= 5000:
            category = "LOW PAYMENT CATEGORY"

        elif final_amount <= 15000:
            category = "MEDIUM PAYMENT CATEGORY"

        else:
            category = "HIGH PAYMENT CATEGORY"

        # Display billing receipt
        print("\n======================================")
        print("          BILLING RECEIPT")
        print("======================================")

        print("Patient Name       :", name)
        print("Patient Age        :", age)

        print("--------------------------------------")
        print("Consultation       : ₹", consultation)
        print("Diagnostic         : ₹", diagnostic)
        print("Treatment          : ₹", treatment)

        print("--------------------------------------")
        print("Gross Bill         : ₹", gross_bill)
        print("Senior Discount    : ₹", senior_discount)
        print("Card Discount      : ₹", card_discount)
        print("Total Concession   : ₹", total_discount)

        print("--------------------------------------")
        print("Final Payable      : ₹", final_amount)

        print("--------------------------------------")
        print("Patient Category   :", category)

        print("======================================")
        print("       BILLING COMPLETED")
        print("======================================")

    except ValueError as e:
        print("Invalid Input:", e)


# Main program
hospital_billing()

