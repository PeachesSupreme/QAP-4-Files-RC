# Program to enter and calculate new insurance policy information for the customers of
# One Stop Insurance Company

# Author: Ryan Crowley
# Date: March 22nd, 2023

# Import Libraries
import datetime

# Constants  Read from OSICDef.dat
f = open('OSICDef.dat','r')
POLICY_NUM = int(f.readline())
BASIC_AUTO_RATE = float(f.readline())
ADD_AUTO_DISC = float(f.readline())
EXTRA_LIAB = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR = float(f.readline())
HST = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

MONTH_PROGRAM = 8

while True:
    # Input for customers information, mailing address
    while True:
        custFirstName = input("Enter the customer's first name: ").title()
        if custFirstName == "":
            print("Cannot be left blank, input valid name.")
        else:
            break

    while True:
        custLastName = input("Enter the customer's last name: ").title()
        if custLastName == "":
            print("Cannot be left blank, input valid name.")
        else:
            break

    while True:
        phoneNum = input("Enter the customer's phone number (XXX-XXX-XXXX): ")
        if phoneNum == "":
            print("Cannot be left blank, input valid phone number.")

        elif len(phoneNum) != 12:
            print("Phone number too long or too short, input valid phone number.")

        elif phoneNum[3] != "-" or phoneNum[7] != "-":
            print("Must be a hyphen seperating numbers, input valid phone number.")

        elif not phoneNum[:3].isdigit():
            print("Phone number must contain only numbers, input valid phone number.")
        elif not phoneNum[4:6].isdigit():
            print("Phone number must contain only numbers, input valid phone number.")
        elif not phoneNum[-3:].isdigit():
            print("Phone number must contain only numbers, input valid phone number.")
        else:
            break

    while True:
        custAddress = input("Enter the customer's street address:")
        if custAddress == "":
            print("Cannot be left blank, input valid street address.")
        else:
            break

    while True:
        custCity = input("Enter the customer's city of residence:").title()
        if custCity == "":
            print("Cannot be left blank, input valid city.")
        else:
            break

    while True:
        provList = ["YT", "NT", "NU", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL"]
        custProv = input("Enter the customer's province (XX):").upper()
        if custProv == "":
            print("Cannot be left blank, input valid province.")

        elif len(custProv) != 2:
            print ("Use abbreviation for province, enter valid province.")

        elif not custProv in provList :
            print("Invalid province name, input valid province ")
        else:
            break

    while True:
        custPostCode = input("Enter the customer's postal code (X#X#X#):").upper()
        if custPostCode == "":
            print("Cannot be left blank, input valid postal code.")

        elif len(custPostCode) != 6 :
            print("Not a valid postal code, input valid postal code.")

        elif not custPostCode[0].isalpha():
            print("Must be a letter, enter valid postal code.")
        elif not custPostCode[2].isalpha():
            print("Must be a letter, enter valid postal code.")
        elif not custPostCode[4].isalpha():
            print("Must be a letter, enter valid postal code.")
        elif  not custPostCode[1].isdigit():
            print("Must be a number, enter valid postal code.")
        elif not custPostCode[3].isdigit():
            print("Must be a number, enter valid postal code.")
        elif not custPostCode[5].isdigit():
            print("Must be a number, enter valid postal code.")

        else:
            break

    # Inputs for insurance policy information
    while True:
        try:
            numCars = int(input("Enter the total number of cars to be insured:"))
        except:
            print("Number of cars is invalid, enter valid number of cars.")
        else:
            break

    while True:
        extraLiab = input("Does customer want extra liability coverage (Y/N): ").upper()
        yesOrNo = ["Y", "N"]
        if extraLiab == "":
            print("Cannot be left blank, input Y for yes or N for no.")
        elif not extraLiab in yesOrNo :
            print("Enter Y for yes or N for no.")
        else:
            break

    while True:
        glassCov = input("Does customer want glass coverage (Y/N): ").upper()
        yesOrNo = ["Y", "N"]
        if glassCov == "":
            print("Cannot be left blank, input Y for yes or N for no.")
        elif not glassCov in yesOrNo:
            print("Enter Y for yes or N for no.")
        else:
            break

    while True:
        loanerCov = input("Does customer want loaner car coverage (Y/N): ").upper()
        yesOrNo = ["Y", "N"]
        if loanerCov == "":
            print("Cannot be left blank, input Y for yes or N for no.")
        elif not loanerCov in yesOrNo:
            print("Enter Y for yes or N for no.")
        else:
            break

    while True:
        fullMonthly = input("Does customer want to pay in full or monthly (F/M): ").upper()
        fullOrMonthly = ["F", "M"]
        if fullMonthly == "":
            print("Cannot be left blank, input F for full or M for monthly.")
        elif not extraLiab in yesOrNo:
            print("Enter F for full or M for monthly.")
        else:
            break

    # Calculations for insurance policy cost
    addCars = numCars - 1
    discPrice = BASIC_AUTO_RATE - (BASIC_AUTO_RATE * ADD_AUTO_DISC)
    insurPrem = BASIC_AUTO_RATE + (addCars * discPrice)

    if extraLiab == "Y":
        extraLiabCost = numCars * EXTRA_LIAB
    else:
        extraLiabCost = 0

    if glassCov == "Y":
        glassCovCost = numCars * GLASS_COV
    else:
        glassCovCost = 0

    if loanerCov == "Y":
        loanerCovCost = numCars * LOANER_CAR
    else:
        loanerCovCost = 0

    extraCosts = extraLiabCost + glassCovCost + loanerCovCost
    totalPremium = insurPrem + extraCosts
    salesTax = HST * totalPremium
    totalCost = totalPremium + salesTax

    # total for monthly cost
    totalPremiumM = PROCESS_FEE + insurPrem + extraCosts
    totalCostM = totalPremiumM + (HST * totalPremium)
    monthlyCost = totalCost/MONTH_PROGRAM

    # setting up dates for invoices
    invoiceDate = datetime.datetime.now()
    invoiceDate = invoiceDate.strftime("%m,%d,%Y")
    nextPayDate =  ""

    nextMonth = datetime.datetime.now()
    nextMonth = (nextMonth.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    nextMonth = nextMonth.strftime("%m,%d,%Y")

    print()
    print()
    print("*" * 103)
    print(" "*39, "One Stop Insurance Company")
    print(" "*29, "Customer Insurance Policy Information & Invoice")
    print("*" * 103)
    print()
    print("  ", "Policy Number: " + str(POLICY_NUM))
    print()
    print("  ", "Customer information:", " "*35, "Policy information:")
    print("  ", "---------------------", " "*35, "-------------------")
    print("  ", "Name:         " + f"{ custFirstName + ' ' + custLastName:<43s}", "Number of automobiles:        " + str(numCars))

    # variable for print statement
    # extra liability
    if extraLiab == "Y":
        liabChoice = "Yes"
    else :
        liabChoice = "Declined"
    print("  ", "Phone number: " + f"{phoneNum:<43s}", "Extra liability coverage:     "+ liabChoice)

    # glass coverage
    if glassCov == "Y":
        glassChoice = "Yes"
    else :
        glassChoice = "Declined"
    print("  ", "Address:      " + f"{custAddress:<43s}", "Optional glass coverage:      " + glassChoice)

    # loaner car coverage
    if loanerCov == "Y":
        loanerChoice = "Yes"
    else :
        loanerChoice = "Declined"
    print("  ", "City:         " + f"{custCity:<43s}", "Optional loaner car coverage: " + loanerChoice)
    print("  ", "Province:     " + custProv)
    print("  ", "Postal code:  " + custPostCode)
    print()

    print("*" * 103)
    print()
    print(" "*44, "Policy Summary:")
    print(" "*44, "---------------")
    print(" "*39, "Invoice Date: " + invoiceDate )
    print()

    # format prices to print properly
    BASIC_AUTO_RATEDsp = "${:,.2f}".format(BASIC_AUTO_RATE)
    print("  ", "Initial automobile coverage:    " + f"{BASIC_AUTO_RATEDsp:>10s}", " "*14, "Method of Payment:")

    monthlyCostDsp = "${:,.2f}".format(monthlyCost)
    totalCostDsp = "${:,.2f}".format(totalCost)
    if fullMonthly == "F":
        payChoice = str("Full payment of ") + str(f"{totalCostDsp}")
    else:
        payChoice = str("Monthly payments of ") + str(f"{monthlyCostDsp}")
    if addCars == 0:
        print("  ", "Additional automobile coverage:        N/A" + " "*15, payChoice )

    else:
        numChoice = addCars * discPrice
        numChoiceDsp = "${:,.2f}".format(numChoice)
        print("  ", "Additional automobile coverage: " + f"{numChoiceDsp:>10s}" + " "*15, payChoice )

    if fullMonthly == "F":
        payChoice2 = str("Balance paid ") + str(invoiceDate)
    else:
        payChoice2 = str("Next payment due ") + str(nextMonth)
    if extraLiabCost == 0 :
        print("  ", "Extra liability coverage:              N/A" + " "*15, payChoice2)
    else:
        extraLiabCostDsp = "${:,.2f}".format(extraLiabCost)
        print("  ", "Extra liability coverage:       " + f"{extraLiabCostDsp:>10s}" + " "*15, payChoice2)

    if glassCovCost == 0:
        print("  ", "Glass coverage:                        N/A")
    else:
        glassCovCostDsp = "${:,.2f}".format(glassCovCost)
        print("  ", "Glass coverage:                 " + f"{glassCovCostDsp:>10s}")

    if loanerCovCost == 0:
        print("  ", "Loaner car coverage:                   N/A")
    else:
        loanerCovCostDsp = "${:,.2f}".format(loanerCovCost)
        print("  ", "Loaner car coverage:            " + f"{loanerCovCostDsp:>10s}")

    totalPremiumDsp = "${:,.2f}".format(totalPremium)
    print("  ", "Premium total:                  " + f"{totalPremiumDsp:>10s}")

    salesTaxDsp = "${:,.2f}".format(salesTax)
    print("  ", "Sales tax:                      " + f"{salesTaxDsp:>10s}")
    print(" "*34, "----------")


    print("  ", "Total cost:                     " + f"{totalCostDsp:>10s}")


    # writing values for policy information to Policies.dat
    f = open('Policies.dat', 'a')
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(str(invoiceDate)))
    f.write("{}, ".format(str(custFirstName)))
    f.write("{}, ".format(str(custLastName)))
    f.write("{}, ".format(str(custAddress)))
    f.write("{}, ".format(str(custCity)))
    f.write("{}, ".format(str(custProv)))
    f.write("{}, ".format(str(custPostCode)))
    f.write("{}, ".format(str(phoneNum)))
    f.write("{}, ".format(str(numCars)))
    f.write("{}, ".format(str(extraLiab)))
    f.write("{}, ".format(str(glassCov)))
    f.write("{}, ".format(str(loanerCov)))
    f.write("{}, ".format(str(fullMonthly)))
    f.write("{}\n ".format(str(totalPremium)))
    f.close()

    # writing the values back to the defaults file
    f = open('OSICDef.dat', 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n" .format(str(BASIC_AUTO_RATE)))
    f.write("{}\n".format(str(ADD_AUTO_DISC)))
    f.write("{}\n".format(str(EXTRA_LIAB)))
    f.write("{}\n".format(str(GLASS_COV)))
    f.write("{}\n".format(str(LOANER_CAR)))
    f.write("{}\n".format(str(HST)))
    f.write("{}\n".format(str(PROCESS_FEE)))
    f.close()

    print()
    print("Policy information processed and saved.")
    POLICY_NUM += 1

    print()
    exitInvoice = input("Continue with next invoice (Y for yes, END to quit): ").upper()
    if exitInvoice == "END":
        exit()

    print()
    print()




