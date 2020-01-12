#Hello, this is a simple code to calculate yearly profit for 2019.
print "Welcome to the 2019 Profit Calculator!"
print "This tool will allow input of monthly data, compile it into quarterly data, and calculate year-end totals."

print "Let's get to know each other."
name = raw_input("What is your company's name?")
print "It's nice to meet you, %s! Let's get some information from you." % (name)
#This first section takes first quarter profits and expenses and outputs monthly and first quarter totals.
january_revenue = 1000
january_expenses = 200
january_profit = january_revenue - january_expenses
print "Your profit for January 2019 is $" + str(january_profit)
february_revenue = 3000
february_expenses = 700
february_profit = february_revenue - february_expenses
print "Your profit for February 2019 is $" + str(february_profit)
march_revenue = 7000
march_expenses = 400
march_profit = march_revenue - march_expenses
print "Your profit for March 2019 is $" + str(march_profit)
#This next section will add all of the expenses and profits for the first quarter of the year.
quarter_1_expenses = january_expenses + february_expenses + march_expenses
quarter_1_profits = january_profit + february_profit + march_profit
print "Expenses are stacking up in the first quarter. Take a look at what you spent:"
print "Your total expenses for the first quarter were $" + str(quarter_1_expenses)
print "Yikes!"
print "However, you did a great job making profit."
print "Your first quarter profits are $" + str(quarter_1_profits)
print "Great job!"


#Second quarter values
april_revenue = 1000
april_expenses = 800
april_profit = april_revenue - april_expenses
print "Your profit for April 2019 is $" + str(april_profit)
may_revenue = 1500
may_expenses = 800
may_profit = may_revenue - may_expenses
print "Your profit for May 2019 is $" + str(may_profit)
june_revenue = 1800
june_expenses = 600
june_profit = june_revenue - june_expenses
print "Your profit for June 2019 is $" + str(june_profit)
#Second quarter totals
quarter_2_expenses = april_expenses + may_expenses + june_expenses
quarter_2_profits = april_profit + may_profit + june_profit
print "Let's take a look at how you did in the second quarter of 2019."
print "Your second quarter expenses were $" + str(quarter_2_expenses)
print "Wow!"
print "Now, for the most important information:"
print "Your Quarter 2 profits are $" + str(quarter_2_profits)
print "That's terrible. See if you can do better next quarter."


#Third quarter values
july_revenue = 2500
july_expenses = 600
july_profit = july_revenue - july_expenses
print "Your profit for July 2019 is $" + str(july_profit)
august_revenue = 3000
august_expenses = 550
august_profit = august_revenue - august_expenses
print "Your profit for August 2019 is $" + str(august_profit)
september_revenue = 4000
september_expenses = 650
september_profit = september_revenue - september_expenses
print "Your profit for September 2019 is $" + str(september_profit)
#Third quarter totals
quarter_3_profits = july_profit + august_profit + september_profit
quarter_3_expenses = july_expenses + august_expenses + september_expenses
print "Are you ready for your third quarter totals?"
print "Let's see how you did."
print "Your third quarter expenses are $" + str(quarter_3_expenses)
print "Much better!"
print "Your third quarter profits are $" + str(quarter_3_profits)
print "What an improvement!"


#Fourth quarter values
october_revenue = 5000
october_expenses = 750
october_profit = october_revenue - october_expenses
print "Your profit for October 2019 is $" + str(october_profit)
november_revenue = 6000
november_expenses = 800
november_profit = november_revenue - november_expenses
print "Your profit for November 2019 is $" + str(november_profit)
december_revenue = 10000
december_expenses = 700
december_profit = december_revenue + december_expenses
print "Your profit for December 2019 is $" + str(december_profit)
#Fourth quarter totals
quarter_4_expenses = october_expenses + november_expenses + december_expenses
quarter_4_profits = october_profit + november_profit + december_profit
print "Let's finish the year strong! How did you do?"
print "Your fourth quarter expenses were $" + str(quarter_4_expenses)
print "Nice job reigning in your spending!"
print "Drumroll please!"
print "Your fourth quarter profits were $" + str(quarter_4_profits)
print "Amazing!"

#Year 2019 totals for all four quarters
total_2019_expenses = quarter_1_expenses + quarter_2_expenses + quarter_3_expenses + quarter_4_expenses
total_2019_profit = quarter_1_profits + quarter_2_profits + quarter_3_profits + quarter_4_profits
print "Let's see how much money you spent in 2019."
print "Your total 2019 expenses were $" + str(total_2019_expenses)
print "Not too bad."
print "Finally, your total 2019 profit is $" + str(total_2019_profit)
print "What a great year!"