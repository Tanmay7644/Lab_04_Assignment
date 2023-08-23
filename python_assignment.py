class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightDatabase:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result
    
    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result
    
    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_db = FlightDatabase()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_db.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("\nSearch Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            city = input("Enter the city code: ")
            city_flights = flight_db.search_by_city(city)
            if city_flights:
                print("\nFlights for", cities[city])
                for flight in city_flights:
                    print(f"Flight ID: {flight.flight_id}, To: {cities[flight.destination]}, Price: {flight.price}")
            else:
                print("No flights found for the given city.")
        
        elif choice == 2:
            source = input("Enter the source city code: ")
            source_flights = flight_db.search_by_source(source)
            if source_flights:
                print("\nFlights from", cities[source])
                for flight in source_flights:
                    print(f"Flight ID: {flight.flight_id}, To: {cities[flight.destination]}, Price: {flight.price}")
            else:
                print("No flights found from the given source city.")
        
        elif choice == 3:
            source = input("Enter the source city code: ")
            destination = input("Enter the destination city code: ")
            between_flights = flight_db.search_between_cities(source, destination)
            if between_flights:
                print("\nFlights between", cities[source], "and", cities[destination])
                for flight in between_flights:
                    print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
            else:
                print("No flights found between the given cities.")
        
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
