#calculates distance and speed of a route and determins what route is faster
#5/29/2025
#CSC121 m1Lab2-Review
#Allen Gaines
def calculate_route(route_num):
    
    while True:
        try:
            
            distance = float(input(f"Enter route {route_num} distance (miles) "))
            speed = float(input(f"Enter route {route_num} speed (mph) "))
            
            
            if distance < 0 or speed <= 0:
                print("Distance and speed must be positive numbers.")

                continue
            # Calculate time in minutes
            
            time = (distance / speed)*60  # Convert time to minutes
           
            return time
            

        except ValueError: 
            print("Invalid input. Please enter numeric values for distance and speed.") 
    



def main():
    print("Welcome to the Route Time Calculator!")
    print("~~~~"*25)
    keep_going = 'yes'
    route_num = 1  # Initialize route number
    
    while keep_going := 'yes':
        fastest_route = None
        fastest_time = None
       

        
        

        print(f"\nCalculating Route {route_num}  :")
        time = calculate_route(route_num)
        
         # Display the time for the current route
         # and check if it's the fastest so far
        print(f"Time for Route {route_num}  : {time:.2f} minutes")
        if fastest_time is None or time < fastest_time:
            fastest_time = time
            fastest_route = route_num
        keep_going = input("Do you want to calculate another set of routes? (yes/no): ").strip().lower()
        
        while keep_going not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            keep_going = input("Do you want to calculate another set of routes? (yes/no): ").strip().lower()
        
        
        

    
        
        
        if keep_going != 'yes':
             if fastest_route is not None:
                print(f"\nRoute {fastest_route} is fastest; {fastest_time:.0f} minutes")
                break
       
                
        else:
            print("Calculating next route...") 
            route_num += 1
            continue
    
        

    

       

if __name__ == "__main__":
    main()



'''BEGIN PROGRAM

DISPLAY "Welcome to the Route Time Calculator!"
DISPLAY decorative line

REPEAT  // Loop to allow multiple sets of route calculations

    REPEAT  // Get a valid number of routes from the user
        PROMPT "How many routes do you want to calculate?"
        READ number_of_routes
        IF number_of_routes is not a positive integer THEN
            DISPLAY "Please enter a positive whole number."
        ELSE
            BREAK loop
        END IF
    END REPEAT

    SET fastest_time = NULL
    SET fastest_route = NULL

    FOR route_number FROM 1 TO number_of_routes DO
        DISPLAY "Calculating Route route_number:"

        REPEAT  // Get valid distance and speed for each route
            PROMPT "Enter distance (miles) for route route_number:"
            READ distance
            PROMPT "Enter speed (mph) for route route_number:"
            READ speed

            IF distance <= 0 OR speed <= 0 THEN
                DISPLAY "Distance and speed must be positive numbers."
            ELSE
                BREAK loop
            END IF
        END REPEAT

        COMPUTE time = (distance / speed) * 60
        DISPLAY "Time for Route route_number: time minutes"

        IF fastest_time is NULL OR time < fastest_time THEN
            SET fastest_time = time
            SET fastest_route = route_number
        END IF
    END FOR

    DISPLAY "Route fastest_route is fastest; fastest_time minutes"

    PROMPT "Do you want to calculate another set of routes? (yes/no):"
    READ user_response
    CONVERT user_response TO lowercase and trim spaces

UNTIL user_response ≠ "yes"

DISPLAY "Goodbye!"
END PROGRAM '''