#Gas Supplier Program
#Group 7 - Kyle , junxian, Mavros
#Oct/14/2023

#Standard Prices for Gas and Oil
oil_cost_litre = 1.27
oil_cost_case = oil_cost_litre * 12
gas_cost_litre = 1.07

#Users chooses the type of Fuel
prompt = ">>>"
print ("-------------------------------------------")
print("***Welcome to Gas Station Supplier Program!***")
print ("-------------------------------------------")
fuel = input(f"Please select the type of purchase:\nG:Gas\nO:Oil\n{prompt}").lower()
#Users chooses litres of gas and Province for tax calculation, Program calculates cost of gas purchase and prints information to screen
if fuel == "g":
    liters_gas = float(input("Enter the number of liters of Gas:"))
    province = input("Please enter the 2 letters province abbreviation:").lower()
    
    if province == "ab" or province == "bc" or province == "mb" or province == "nt" or province == "nu"  or province == "qc" or province == "sk" or province == "yt":
        tax = .05
    elif province == "on":
        tax = .13
    else:
        tax = .15
    if liters_gas <= 4000:
        gas_cost_before_tax = liters_gas * gas_cost_litre 
        gst = gas_cost_before_tax * tax
        total_gas_cost = gas_cost_before_tax + gst
        print ("--------------------------------------------------------------------------------------")
        print ("Product       # Of Liters   Price Before   Price After       GST    Total Price")
        print (f"Gas               {liters_gas:.2f}        {gas_cost_before_tax:.2f}       {gas_cost_before_tax:.2f}    {gst:.2f}        {total_gas_cost:.2f}")
        print ("--------------------------------------------------------------------------------------")
        print ("Thanks for your Business, Good Bye")
#Discount Gas Calculation
    elif liters_gas > 4000:
        gas_cost_before_tax = liters_gas * gas_cost_litre
        discount_gas = gas_cost_before_tax * .9
        gst = discount_gas * tax
        total_gas_cost = discount_gas + gst
        print ("--------------------------------------------------------------------------------------")
        print ("Product       # Of Liters   Price Before   Price After       GST    Total Price")
        print (f"Gas               {liters_gas:.2f}        {gas_cost_before_tax:.2f}       {discount_gas:.2f}    {gst:.2f}        {total_gas_cost:.2f}")
        print ("--------------------------------------------------------------------------------------")
        print ("Thanks for your Business, Good Bye")
#Users chooses Cases of oil and Province for tax calculation, Program calculates cost of Oil purchase and prints information to screen
elif fuel == "o":
    cases_oil = float(input("Enter the number of cases of Oil:"))
    province = input("Please enter the 2 letters province abbreviation:").lower()
    
    if province == "ab" or province == "bc" or province == "mb" or province == "nt" or province == "nu"  or province == "qc" or province == "sk" or province == "yt":
        tax = .05
    elif province == "on":
        tax = .13
    else:
        tax = .15
    if cases_oil <= 8:
        liter_oil = cases_oil * 12
        oil_cost_before_tax = oil_cost_case * cases_oil
        gst = oil_cost_before_tax * tax
        total_oil_cost = oil_cost_before_tax + gst

        print ("--------------------------------------------------------------------------------------")
        print ("Product       # Of Liters   Price Before   Price After       GST    Total Price")
        print (f"Oil                 {liter_oil:.2f}          {oil_cost_before_tax:.2f}         {oil_cost_before_tax:.2f}      {gst:.2f}          {total_oil_cost:.2f}")
        print ("--------------------------------------------------------------------------------------")
        print ("Thanks for your Business, Good Bye")
#Discount oil Calculation
    elif cases_oil > 8:
        liter_oil = cases_oil * 12
        oil_cost_before_tax = oil_cost_case * cases_oil
        discount_oil = oil_cost_before_tax * .9
        gst = discount_oil * tax
        total_oil_cost = discount_oil + gst

        print ("--------------------------------------------------------------------------------------")
        print ("Product       # Of Liters   Price Before   Price After       GST    Total Price")
        print (f"Oil               {liter_oil:.2f}         {oil_cost_before_tax:.2f}        {discount_oil:.2f}      {gst:.2f}         {total_oil_cost:.2f}")
        print ("--------------------------------------------------------------------------------------")
        print ("Thanks for your Business, Good Bye")
#Invalid Input Print statement
else:
    print ("Invalid input, you should enter g/G or o/O")