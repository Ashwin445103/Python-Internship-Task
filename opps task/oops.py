
from abc import ABC, abstractmethod


class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__seats = seats
        self.__fare = fare

    def display(self):
        print(self.__code, "|", self.__airline, "|",
              self.__source, "to", self.__destination,
              "| Seats:", self.__seats, "| Fare: Rs.", self.__fare)

    def get_code(self):
        return self.__code

    def get_airline(self):
        return self.__airline

    def get_seats(self):
        return self.__seats

    def get_fare(self):
        return self.__fare

    def get_details(self):
        return self.__source + " to " + self.__destination

    def book_seats(self, count):
        self.__seats -= count


class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class RegularPassenger(Passenger):
    def get_discount(self):
        return 0

    def get_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_type(self):
        return "Student"


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets,
                 subtotal, discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def display_summary(self):
        print("\n--- Booking Summary ---")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.get_code(), "|",
              self.flight.get_details())
        print("Airline:", self.flight.get_airline())
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", self.passenger.get_type())
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.get_fare())
        print("Subtotal: Rs.", self.subtotal)
        print("Discount:", int(self.passenger.get_discount() * 100),
              "% = Rs.", self.discount)
        print("Final amount: Rs.", self.total)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Ashwin Air", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "Ashwin Air", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN103", "Ashwin Air", "Pune", "Hyderabad", 25, 2500)
        ]
        self.latest_booking = None
        self.booking_number = 1001

    def display_flights(self):
        print("\n--- Available Flights ---")
        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.get_code() == code.upper():
                return flight
        return None

    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            return "Invalid flight code."
        if not name.strip():
            return "Passenger name cannot be blank."
        if age <= 0:
            return "Age must be greater than 0."
        if tickets <= 0:
            return "Ticket count must be greater than 0."
        if tickets > flight.get_seats():
            return "Not enough seats available."
        return "OK"

    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.get_fare() * tickets
        discount = subtotal * passenger.get_discount()
        total = subtotal - discount
        return subtotal, discount, total

    def confirm_booking(self, flight, passenger, tickets,
                        subtotal, discount, total):
        booking_id = "BK" + str(self.booking_number)

        booking = Booking(
            booking_id, flight, passenger, tickets,
            subtotal, discount, total
        )

        flight.book_seats(tickets)
        self.latest_booking = booking
        self.booking_number += 1

        print("\nBooking confirmed!")
        booking.display_summary()

    def book_flight(self):
        try:
            code = input("Enter flight code: ").strip()
            flight = self.find_flight(code)

            name = input("Enter passenger name: ").strip()
            age = int(input("Enter age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))

            if passenger_type == "student":
                passenger = StudentPassenger(name, age)
            elif passenger_type == "regular":
                passenger = RegularPassenger(name, age)
            else:
                print("Invalid passenger type.")
                return

            error = self.validate_booking(flight, name, age, tickets)

            if error != "OK":
                print("Booking failed:", error)
                print("No booking was created.")
                return

            subtotal, discount, total = self.calculate_fare(
                flight, passenger, tickets
            )

            self.confirm_booking(
                flight, passenger, tickets,
                subtotal, discount, total
            )

        except ValueError:
            print("Invalid input. Enter a valid age and ticket count.")
            print("No booking was created.")

    def view_booking(self):
        if self.latest_booking is None:
            print("No booking found. Please book a flight first.")
        else:
            self.latest_booking.display_summary()

    def run(self):
        print("Welcome to Ashwin Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please select 1 to 4.")


app = FlightBookingSystem()
app.run()
