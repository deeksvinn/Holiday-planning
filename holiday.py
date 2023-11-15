# Program to calculate the user's holiday cost including the plane cost,hotel cost and car rental cost. 
city_flight = input('''Enter the city you would like to fly to
                       Berlin
                       Paris
                       Toronto\n''' ).upper()     
try:
    num_nights = int(input("Enter the number of nights you would like to stay in the hotel: "))
except ValueError:    
    print("Number of nights can only be numbers.")
    exit()
try:    
    rental_days = int(input("How many number of days you would like to hire the car: "))
except ValueError:
    print("Number of rental days can only be numbers")
    exit()

# Function to calculate the hotel cost for the number of nights entered.       
def hotel_cost(num_nights):
    total_cost = num_nights*100
    return total_cost

# Function to calculate the cost of plane tickets. 
def plane_cost(city_flight):
    if city_flight == "BERLIN":
        cost_flight = 800
        return cost_flight
    elif city_flight == "PARIS":
        cost_flight = 300 
        return cost_flight
    elif city_flight == "TORONTO":
        cost_flight = 1200
        return cost_flight
    else:
        print("Sorry , I can't book tickets to any other city except for the options given.")
        exit()

# Function to calculate the car rental for the number of days car needed.
def car_rental(rental_days):
    total_cost_car_rental = rental_days * 150
    return total_cost_car_rental

# Function to calculate the total cost for holiday.
def holiday_cost(hotel_cost_final,plane_cost_final,car_rental_final):
    plane_cost_final = plane_cost(city_flight)
    print(f"\nThe costs involved for the holiday to {city_flight} are as follows:")
    print(f"The cost of flight tickets is :{plane_cost_final}")
    hotel_cost_final = hotel_cost(num_nights)
    print(f"The cost of hotel for {num_nights} nights stay is :{hotel_cost_final}")
    car_rental_final = car_rental(rental_days)
    print(f"The cost of car rental for {rental_days} days is :{car_rental_final}")
    total_cost = hotel_cost_final + plane_cost_final + car_rental_final
    print(f"The total cost for the holiday is {total_cost}\n")

# Calling the function for given inputs.
holiday_cost(num_nights,city_flight,rental_days)