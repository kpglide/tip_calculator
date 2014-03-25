from optparse import OptionParser
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    tip_value=tip_value,
                    total = total)
    return meal_info
 
 
def main():
    parser = OptionParser()
    parser.add_option("-m", "--meal", dest="meal", help="base cost of meal")
    parser.add_option("-x", "--tax", dest="tax_percent")
    parser.add_option("-t", "--tip", dest="tip_percent", 
                        help="percent tip you want to leave", default=0.20)  
                        #let's accrue good karma by defaulting to a decent 20%
                        #tip!
    (options, args) = parser.parse_args()
    if not options.meal:
        parser.error("You forgot to indicate the base cost of your meal!")
    while True:
        try:
            options.meal = float(options.meal)
            break
        except ValueError:
            options.meal = raw_input('--meal cost must be a positive numeric value.  --meal: ')
    if not options.tax_percent:
        parser.error("You forgot to indicate the tax rate!")
    while True:
        try:
            options.tax_percent = float(options.tax_percent)
            break
        except ValueError:
            options.tax_percent = raw_input('--tax must be a positive decimal value.  --tax: ')
    while True:
        try:
            options.tip_percent = float(options.tip_percent)
            break
        except ValueError:
            options.tip_percent = raw_input('--tip must be a positive decimal value.  --tip: ')
    meal_info = calculate_meal_costs(options.meal, options.tax_percent, 
                                    options.tip_percent)
 
    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*meal_info['tip_rate']), 
                                        meal_info['tip_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()
