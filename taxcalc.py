#Tax Calculator
def taxCalc(price, tax):

    addedtax = price * tax
    trueprice = addedtax + price
    print "Tax: ", format(addedtax,'.2f'), "Total Price: ", format(trueprice, '.2f')

taxCalc(79.83, .35)
