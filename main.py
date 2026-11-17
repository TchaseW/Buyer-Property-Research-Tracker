import json

class Property:

    def __init__(self, property_id, address, city, state, price,
                 bedrooms, bathrooms, square_feet, property_type, lot_size, property_category):
        self.property_id = property_id
        self.address = address
        self.city = city
        self.state = state
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_feet = square_feet
        self.property_type = property_type
        self.lot_size = lot_size
        self.property_category = property_category

    def display_details(self):
        print(f"Property ID: {self.property_id}")
        print(f"Address: {self.address}")
        print(f"Location: {self.city}, {self.state}")
        print(f"Price: ${self.price:,.2f}")
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")
        print(f"Square Feet: {self.square_feet}")
        print(f"Property Type: {self.property_type}")
        print(f"Lot Size: {self.lot_size} acres")
        print(f"Property Category: {self.property_category}")


class Buyer:
    def __init__(self, buyer_id, name, locations, max_budget,
                 min_bedrooms, property_types):

        self.buyer_id = buyer_id
        self.name = name
        self.locations = locations
        self.max_budget = max_budget
        self.min_bedrooms = min_bedrooms
        self.property_types = property_types
        self.saved_properties = []
        self.favorites = []

    def display_details(self):
        print(f"Buyer ID: {self.buyer_id}")
        print(f"Name: {self.name}")
        print(f"Preferred Locations: {', '.join(self.locations)}")
        print(f"Maximum Budget: ${self.max_budget:,.2f}")
        print(f"Minimum Bedrooms: {self.min_bedrooms}")
        print(f"Preferred Property Types: {', '.join(self.property_types)}")
        print(f"Saved Properties: {len(self.saved_properties)}")
        print(f"Favorites: {len(self.favorites)}")
        
    def save_property(self, property):
        if property not in self.saved_properties:
            self.saved_properties.append(property)
            print(f"{property.address} saved for {self.name}.")
        else:
            print("This property is already saved.")
            
    def add_favorite(self, property):
        if property in self.saved_properties:
            if property not in self.favorites:
                self.favorites.append(property)
                print(f"{property.address} added to {self.name}'s favorites.")
            else:
                print("This property is already a favorite.")
        else:
            print("Save this property before adding it to favorites.")
            
    def display_saved_properties(self):
        if not self.saved_properties:
            print(f"{self.name} has no saved properties.")
            return

        print(f"\n--- {self.name.upper()}'S SAVED PROPERTIES ---")

        for property in self.saved_properties:
            print(f"{property.address} - ${property.price:,}")
            
    def display_favorites(self):
        if not self.favorites:
            print(f"{self.name} has no favorite properties.")
            return

        print(f"\n--- {self.name.upper()}'S FAVORITES ---")

        for property in self.favorites:
            print(f"{property.address} - ${property.price:,}")
            
class PropertyTracker:
    def __init__(self):
        self.buyers = []
        self.properties = []
        
    def add_buyer(self, buyer):
        self.buyers.append(buyer)
        print(f"{buyer.name} added to the tracker.")

    def add_property(self, property):
        self.properties.append(property)
        print(f"{property.address} added to the tracker.")
        
    def add_property_from_input(self):
        address = input("Enter property address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        while True:
            try:
                price = float(input("Enter asking price: "))
                break
            except ValueError:
                print("Please enter a valid number for the asking price.")
        while True:
            try:
                bedrooms = int(input("Enter number of bedrooms: "))
                break
            except ValueError:
                print("Please enter a valid whole number for bedrooms.")
        while True:
            try:
                bathrooms = float(input("Enter number of bathrooms: "))
                break
            except ValueError:
                print("Please enter a valid number for bathrooms.")
        while True:
            try:
                square_feet = int(input("Enter square footage: "))
                break
            except ValueError:
                print("Please enter a valid whole number for square footage.")
        property_type = input("Enter property type: ")
        while True:
            try:
                lot_size = float(input("Enter lot size in acres: "))
                break
            except ValueError:
                print("Please enter a valid number for lot size.")
        property_category = input("Enter category (Residential or Land): ")
        new_property = Property(max([property.property_id for property in self.properties], default=0) + 1, address, city, state, price, bedrooms, bathrooms, square_feet, property_type, lot_size, property_category)
        
        self.add_property(new_property)
        self.save_properties()
        
    def save_property_for_buyer(self):
        print("\nAvailable Buyers:")

        for buyer in self.buyers:
            print(f"{buyer.buyer_id}. {buyer.name}")

        buyer_id = int(input("Enter buyer ID: "))

        for buyer in self.buyers:
            if buyer.buyer_id == buyer_id:
                print("\nAvailable Properties:")

                for property in self.properties:
                    print(f"{property.property_id}. {property.address} - ${property.price:,}")

                property_id = int(input("Enter property ID: "))

                for property in self.properties:
                    if property.property_id == property_id:
                        buyer.save_property(property)
                        self.save_buyers()
                        return

                print("Property not found.")
                return

        print("Buyer not found.")
        
    def display_all_properties(self):
        if not self.properties:
            print("No properties have been added.")
            return

        print("\n--- ALL TRACKED PROPERTIES ---")

        for property in self.properties:
            print("-------------------------")
            property.display_details()
    
    def search_by_city(self, city):
        results = []

        for property in self.properties:
            if property.city.lower() == city.lower():
                results.append(property)

        if not results:
            print(f"No properties found in {city}.")
            return

        print(f"\n--- PROPERTIES IN {city} ---")

        for property in results:
            property.display_details()
            print("-------------------------")
            
    def search_by_price(self, max_price):
        results = []

        for property in self.properties:
            if property.price <= max_price:
                results.append(property)

        if not results:
            print(f"No properties found under ${max_price:,}.")
            return

        print(f"\n--- PROPERTIES UNDER ${max_price:,} ---")

        for property in results:
            print(f"{property.address} - ${property.price:,}")
            
    def search_by_type(self, property_type):
        results = []

        for property in self.properties:
            if property.property_type.lower() == property_type.lower():
                results.append(property)

        if not results:
            print(f"No properties found of type {property_type}.")
            return

        print(f"\n--- {property_type.upper()} PROPERTIES ---")

        for property in results:
            print(f"{property.address} - {property.property_type}")
            
    def advanced_search(self, city=None, max_price=None,
                        min_bedrooms=None, property_type=None,
                        property_category=None, min_lot_size=None):

        results = []

        for property in self.properties:

            if city and property.city.lower() != city.lower():
                continue

            if max_price is not None and property.price > max_price:
                continue

            if min_bedrooms is not None and property.bedrooms < min_bedrooms:
                continue

            if property_type and property.property_type.lower() != property_type.lower():
                continue

            if property_category and property.property_category.lower() != property_category.lower():
                continue

            if min_lot_size is not None and property.lot_size < min_lot_size:
                continue

            results.append(property)

        print(f"\n--- ADVANCED SEARCH RESULTS ({len(results)} found) ---")

        if not results:
            print("No properties matched your search.")
            return

        for property in results:
            print(f"{property.address} - ${property.price:,}")
            
    def display_menu(self):
        print("\n===== BUYER PROPERTY RESEARCH TRACKER =====")
        print("1. Add a property")
        print("2. View all properties")
        print("3. Search properties by city")
        print("4. Search properties by maximum price")
        print("5. Search properties by type")
        print("6. View a buyer's saved properties")
        print("7. View a buyer's favorites")
        print("8. Save a property for a buyer")
        print("9. Add a property to favorites")
        print("10. Exit")
        
    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_property_from_input()

            elif choice == "2":
                self.display_all_properties()
            
            elif choice == "3":
                city = input("Enter the city: ")
                self.search_by_city(city)
                
            elif choice == "4":
                max_price = float(input("Enter the maximum price: "))
                self.search_by_price(max_price)
                
            elif choice == "5":
                property_type = input("Enter the property type: ")
                self.search_by_type(property_type)
                
            elif choice == "6":
                print("\nAvailable Buyers:")

                for buyer in self.buyers:
                    print(f"{buyer.buyer_id}. {buyer.name}")

                buyer_id = int(input("Enter the buyer ID: "))

                for buyer in self.buyers:
                    if buyer.buyer_id == buyer_id:
                        buyer.display_saved_properties()
                        
            elif choice == "7":
                print("\nAvailable Buyers:")

                for buyer in self.buyers:
                    print(f"{buyer.buyer_id}. {buyer.name}")

                buyer_id = int(input("Enter the buyer ID: "))

                for buyer in self.buyers:
                    if buyer.buyer_id == buyer_id:
                        buyer.display_favorites()
                        
            elif choice == "8":
                self.save_property_for_buyer()

            elif choice == "9":
                print("\nAvailable Buyers:")

                for buyer in self.buyers:
                    print(f"{buyer.buyer_id}. {buyer.name}")

                buyer_id = int(input("Enter buyer ID: "))

                for buyer in self.buyers:
                    if buyer.buyer_id == buyer_id:
                        print("\nAvailable Properties:")

                        for property in self.properties:
                            print(f"{property.property_id}. {property.address}")

                        property_id = int(input("Enter property ID: "))

                        for property in self.properties:
                            if property.property_id == property_id:
                                buyer.add_favorite(property)
                                self.save_buyers()
                                break

            elif choice == "10":
                print("Exiting Property Tracker. Goodbye!")
                break

            else:
                print("Please enter a valid option.")
            
    def search_for_buyer(self, buyer):
        results = []

        for property in self.properties:

            if property.city.lower() not in [location.lower() for location in buyer.locations]:
                continue

            if property.price > buyer.max_budget:
                continue

            if property.bedrooms < buyer.min_bedrooms:
                continue

            if property.property_type not in buyer.property_types:
                continue

            results.append(property)

        print(f"\n--- PROPERTY MATCHES FOR {buyer.name} ---")

        if not results:
            print("No matching properties found.")
            return

        for property in results:
            print(f"{property.address} - ${property.price:,}")
            
    def save_properties(self):
        property_data = []

        for property in self.properties:
            property_data.append({"property_id": property.property_id, "address": property.address, "city": property.city, "state": property.state, "price": property.price, "bedrooms": property.bedrooms, "bathrooms": property.bathrooms, "square_feet": property.square_feet, "property_type": property.property_type, "lot_size": property.lot_size, "property_category": property.property_category})

        with open("properties.json", "w") as file:
            json.dump(property_data, file, indent=4)

        print("Properties saved successfully!")
        
    
    def load_properties(self):
        try:
            with open("properties.json", "r") as file:
                property_data = json.load(file)

            for data in property_data:
                property = Property(data["property_id"], data["address"], data["city"], data["state"], data["price"], data["bedrooms"], data["bathrooms"], data["square_feet"], data["property_type"], data["lot_size"], data["property_category"])

                self.properties.append(property)

            print("Properties loaded successfully!")

        except FileNotFoundError:
            print("No saved properties found.")

    def save_buyers(self):
        buyer_data = []

        for buyer in self.buyers:
            buyer_data.append({"buyer_id": buyer.buyer_id, "name": buyer.name, "locations": buyer.locations, "max_budget": buyer.max_budget, "min_bedrooms": buyer.min_bedrooms, "property_types": buyer.property_types, "saved_properties": [property.property_id for property in buyer.saved_properties], "favorites": [property.property_id for property in buyer.favorites]})

        with open("buyers.json", "w") as file:
            json.dump(buyer_data, file, indent=4)

        print("Buyers saved successfully!")

    def load_buyers(self):
        try:
            with open("buyers.json", "r") as file:
                buyer_data = json.load(file)

            for data in buyer_data:
                buyer = Buyer(data["buyer_id"], data["name"], data["locations"], data["max_budget"], data["min_bedrooms"], data["property_types"])

                for property_id in data["saved_properties"]:
                    for property in self.properties:
                        if property.property_id == property_id:
                            buyer.saved_properties.append(property)

                for property_id in data["favorites"]:
                    for property in buyer.saved_properties:
                        if property.property_id == property_id:
                            buyer.favorites.append(property)

                self.buyers.append(buyer)

            print("Buyers loaded successfully!")

        except FileNotFoundError:
            print("No saved buyers found.")


buyer1 = Buyer(1, "Sarah", ["Morristown", "Sevierville"], 400000, 3, ["Ranch", "Tudor", "Cottage"])
buyer2 = Buyer(2, "Michael", ["Knoxville", "Jefferson City"], 300000, 2, ["Cottage", "Farmhouse"])

tracker = PropertyTracker()

tracker.load_properties()
tracker.load_buyers()

if not tracker.buyers:
    tracker.add_buyer(buyer1)
    tracker.add_buyer(buyer2)
    tracker.save_buyers()

tracker.run_menu()