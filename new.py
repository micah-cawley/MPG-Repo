def calc():
    roadtrip = float(input("How many miles is your road trip?"))
    mpg = float(input("What is your miles per gallon?"))
    gas_price = float(input("How many dollars does a gallon of gas cost?"))
    #those are our main inputs that you have to enter

    final_price = gas_price*(roadtrip/mpg)
    final_price_currency = f"${final_price:,.2f}"
    #this is the cost of the road trip in gallons of gas
    #to format as currency, make another variable that will assign currency to another variable. Wrap the other variable in f"${VARIABLENAME:,.2f}"
    #enter gas price as $x.xx
    print("The road trip will cost",final_price_currency,"in gas!")

calc()


