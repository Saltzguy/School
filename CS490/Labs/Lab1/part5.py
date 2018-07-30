
class Flight:

    def __init__(self, flight_number, from_location, to_location, depart_time, arrive_time):

        # Type flight_number: Integer
        # Type from_location: String
        # Type to_location: String
        # Type depart_time: String ('mm/dd/yyyy hh:mm AM/PM')
        # Type arrive_time: String ('mm/dd/yyyy hh:mm AM/PM')

        self.__num = flight_number
        self.__from = from_location
        self.__to = to_location
        self.__depart = depart_time
        self.__arrive = arrive_time

    def __str__(self):

        # Return Type: String

        out = 'Flight Number: ' + str(self.__num) + ' (' + self.__from + ' - ' + self.__to + ')\n'
        out = out + 'Depart: ' + self.__depart + ', Arrive: ' + self.__arrive
        return out


class Person:

    def __init__(self, last_name, first_name, date_of_birth):

        # Type last_name: String
        # Type first_name: String
        # Type date_of_birth: String ('mm/dd/yyyy')

        self.__last = last_name
        self.__first = first_name
        self.__dob = date_of_birth

    def __str__(self):

        # Return Type: String

        return self.__first + ' ' + self.__last


class Employee(Person):

    def __init__(self, last_name, first_name, date_of_birth, employee_number):

        # Type last_name: String
        # Type first_name: String
        # Type date_of_birth: String ('mm/dd/yyyy')
        # employee_number: Integer

        super().__init__(last_name, first_name, date_of_birth)
        self.__id = employee_number

    def book_air_ticket(self, traveler, flight):

        # Type traveler: Passenger
        # Type flight: Flight
        # Return Type: AirTicket

        return traveler.book_air_ticket(self, flight)


class Passenger(Person):

    def __init__(self, last_name, first_name, date_of_birth):

        # Type last_name: String
        # Type first_name: String
        # Type date_of_birth: String ('mm/dd/yyyy')

        super().__init__(last_name, first_name, date_of_birth)
        self.__itineraries = []

    def book_air_ticket(self, agent, flight):

        # Type agent: Employee
        # Type flight: Flight
        # Return Type: AirTicket

        ticket = AirTicket(self, agent, flight)
        self.__itineraries.append(ticket)
        return ticket

    def get_tickets(self):

        # Return Type: String

        out = ''
        for ticket in self.__itineraries:
            out = out + str(ticket.verify_payment()) + '\n'
        return out[:-1]


class Itinerary:

    def __init__(self, traveler):

        # Type traveler: Passenger

        self.__owner = traveler

    def get_traveler(self):

        # Return Type: Passenger

        return self.__owner


class Payment:

    def __init__(self, traveler, agent):

        # Type traveler: Passenger
        # Type agent: Employee

        self.__payer = traveler
        self.__payee = agent
        self.__status = 'Pending'

    def verify(self):

        # Return Type: Void

        self.__status = 'Verified'

    def get_status(self):

        # Return Type: Void

        return self.__status


class AirTicket(Itinerary, Payment):  # Multiple Inheritance

    def __init__(self, traveler, agent, flight):

        # Type traveler: Passenger
        # Type agent: Employee
        # Type flight: Flight

        Itinerary.__init__(self, traveler)
        Payment.__init__(self, traveler, agent)
        self.__air = flight

    def verify_payment(self):

        # Return Type: AirTicket

        self.verify()
        return self

    def __str__(self):

        # Return Type: String

        out = 'Passenger Name: ' + str(self.get_traveler()) + '\n'
        out = out + str(self.__air) + '\n'
        out = out + self.get_status()
        return out


def main():

    f1 = Flight(582, 'Kansas City, MO', 'Omaha, NE', '06/15/2018 08:00 am', '06/12/2018 09:00 am')
    f2 = Flight(2354, 'Chicago, IL', 'Tampa, FL', '06/26/2018 01:30 pm', '06/20/2018 04:40 pm')
    f3 = Flight(6666, 'San Francisco, CA', 'Houston, TX', '07/04/2018 09:00 pm', '07/04/2018 11:50 pm')

    p1 = Passenger('Fei', 'Wu', '06/21/1990')
    p2 = Passenger('Yunlong', 'Liu', '06/19/1993')

    a1 = Employee('Ting', 'xia', '10/15/1990', 23606)
    a2 = Employee('Emily', 'Chen', '05/13/1989', 23832)

    a2.book_air_ticket(p1, f1)
    a1.book_air_ticket(p2, f2)
    p1.book_air_ticket(a2, f3)

    print(p1.get_tickets())
    print(p2.get_tickets())


if __name__ == '__main__':
    main()