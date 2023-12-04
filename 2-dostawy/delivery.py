class DestinationAlreadySet(Exception):
    def __init__(self):
        super().__init__("Destination is already set")


class DestinationNotInOffer(Exception):
    def __init__(self):
        super().__init__("Destination is not offered by company")


class DriverIsResting(Exception):
    def __init__(self):
        super().__init__("Driver is resting. They can't drive right now.")


class RideTooLong(Exception):
    def __init__(self):
        super().__init__("Ride will be too long with given hours")


class Delivery:
    def __init__(
        self,
        distance: int = 0,
        destination: str = None,
        hours_since_rest: int = None,
        rest_hours: int = None,
    ):
        self._destination = destination
        self._distance = distance
        self._hours_since_rest = hours_since_rest
        self._rest_hours = rest_hours
        self._destination_dictionary = {
            "Kraków": 290,
            "Gdańsk": 340,
            "Poznań": 312,
            "Rzeszów": 330,
            "Terespol": 197,
        }
        self._home_name = "Warszawa"

    @property
    def distance(self):
        return self._distance

    @property
    def destination(self):
        return self._destination

    @property
    def hours_since_rest(self):
        return self._hours_since_rest

    @property
    def rest_hours(self):
        return self._rest_hours

    @property
    def home_name(self):
        return self._home_name

    def submit_order(self, destination_name):
        if self.destination:
            raise DestinationAlreadySet
        if destination_name not in self._destination_dictionary:
            raise DestinationNotInOffer
        self._destination = destination_name
        self._distance = self._destination_dictionary.get(destination_name)
        self._hours_since_rest = 0
        self._rest_hours = None

    def drive(self, drive_hours: int):
        truck_speed = 80
        if self.rest_hours and self.rest_hours < 3:
            raise DriverIsResting
        self._rest_hours = None
        if self.hours_since_rest + drive_hours > 3:
            raise RideTooLong
        distance_left = self.distance - drive_hours * truck_speed
        if distance_left == 0:
            if self.destination != self.home_name:
                self.start_returning_home()
            else:
                self.reset_after_return()
        else:
            self._distance = distance_left
            self._hours_since_rest = drive_hours

    def rest(self, rest_hours):
        if self.hours_since_rest:
            self._hours_since_rest = 0
            self._rest_hours = rest_hours
        else:
            self._rest_hours += rest_hours

    def start_returning_home(self):
        distance_to_home = self._destination_dictionary.get(self.destination)
        self._destination = self._home_name
        self._hours_since_rest = 0
        self._distance = distance_to_home

    def reset_after_return(self):
        self._destination = None
        self._distance = 0
        self._hours_since_rest = None
        self._rest_hours = None

    def __str__(self):
        destination = self.destination if self.destination else "Not Set"
        distance = self.distance
        hours_since_rest = (
            self.hours_since_rest if self.hours_since_rest else "Unknown"
        )
        rest_hours = self.rest_hours if self.rest_hours else "Unknown"
        return (
            f"Destination: {destination}\n"
            f"Distance: {distance} km\n"
            f"Hours since rest: {hours_since_rest} h\n"
            f"Rest hours: {rest_hours} h"
        )
