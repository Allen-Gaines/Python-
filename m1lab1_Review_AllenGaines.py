# this program is to Write a program that takes as input the number of items, determines the cost per item, and displays the cost per item and total order cost.
#5/27/2025
#CSC121 m1Lab1-Review
#Allen Gaines


keep_going = 'yes'
cost_per_item = 0
while keep_going == 'yes': 
   
    num_items = int(input('Enter the number of items: '))
    #  number of items to there tax value 
    if num_items > 0 and num_items <= 19:
        cost_per_item = 4.75
    elif num_items >= 20 and num_items <= 49:   
        cost_per_item = 4.50
    elif num_items >= 50 and num_items <= 99:   
        cost_per_item = 4.25
    elif num_items >= 100:
        cost_per_item = 4.00
    else:
        print('Invalid number of items. Please enter a number greater than 0.')
        continue
    # Calculate the total cost
    total_cost = num_items * cost_per_item  
    print(f'Cost per item: ${cost_per_item:.2f}')
    print(f'Total order cost: ${total_cost:.2f}')   
    keep_going = input('Do you want to continue? (yes/no): ').lower()
    if keep_going == 'no':
            break
    if keep_going != 'yes' and keep_going != 'no':
        print('Invalid input. Please enter "yes" or "no".')
        keep_going = input('Do you want to continue? (yes/no): ').lower()


        
    
    


print('Thank you for using the program!')

'''Pseudocode for the program

Start Program

Set keep_going to 'yes'

WHILE keep_going is 'yes'
    Prompt user to enter number of items
    Read number_of_items

    IF number_of_items is greater than 0 AND less than or equal to 19 THEN
        Set cost_per_item to 4.75
    ELSE IF number_of_items is between 20 and 49 THEN
        Set cost_per_item to 4.50
    ELSE IF number_of_items is between 50 and 99 THEN
        Set cost_per_item to 4.25
    ELSE IF number_of_items is 100 or more THEN
        Set cost_per_item to 4.00
    ELSE
        Display "Invalid number of items. Please enter a number greater than 0."
        CONTINUE to next iteration

    Calculate total_cost as number_of_items * cost_per_item
    Display "Cost per item" and the cost_per_item
    Display "Total order cost" and the total_cost

    Prompt user: "Do you want to continue? (yes/no)"
    Read keep_going and convert to lowercase

    IF keep_going is 'no' THEN
        BREAK the loop
    ELSE IF keep_going is not 'yes' or 'no' THEN
        Display "Invalid input. Please enter 'yes' or 'no'."
        Prompt again and read keep_going

END WHILE

Display "Thank you for using the program!"

End Program
        
'''

# End of the program'''