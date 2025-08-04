def calculate_ticket_price(age, distance, travel_class):
    # Base rate per mile
    base_rate = 0.5 # base rate in dollars per mile

    # Class multiplier 
    class_multipliers = {
        "economy": 1.0,
        "business": 1.5,
        "first": 2.0
    }

    # Validate class
    travel_class = travel_class.lower()
    if travel_class not in class_multipliers:
        raise ValueError("Invalid travel class. Choose from economy, business, or first.")

    # Calculate base price
    price = distance * base_rate * class_multipliers[travel_class]

    # Apply age-based discounts
    if age < 12:
        price *= 0.5  # 50% discount for children
    elif age >= 60: 
        price *= 0.8  # 20% discount for seniors

    return round(price, 2)

# Example user input
def main():
    try:
        age = int(input("Enter passenger age: "))
        distance = float(input("Enter distance in miles: "))
        travel_class = input("Enter travel class (Economy, Business, or First): ")

        price = calculate_ticket_price(age, distance, travel_class)
        print(f"Total ticket price: ${price}")
    
    except ValueError as e: 
        print (f"Error: {e}")

if __name__ == "__main__":
    main()