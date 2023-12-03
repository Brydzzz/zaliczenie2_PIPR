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

    def submit_order(self, destination_name):
        if self._destination:
            raise DestinationAlreadySet
        if self._destination not in self._destination_dictionary:
            raise DestinationNotInOffer
        self._destination = destination_name
        self._distance = self._destination_dictionary.get(destination_name)
        self._hours_since_rest = 0
        self._rest_hours = None

    def drive(self, drive_hours):
        if self._rest_hours:
            raise DriverIsResting
        if self._hours_since_rest + drive_hours > 3:
            raise RideTooLong
        distance_left = self._distance - drive_hours * 80
        if distance_left == 0:
            if self._destination != self._home_name:
                self.start_returning_home()
            else:
                self.reset_after_return()
        else:
            self._distance = distance_left
            self._hours_since_rest = drive_hours

    def rest(self, rest_hours):
        if self._hours_since_rest:
            self._hours_since_rest = 0
            self._rest_hours = rest_hours
        else:
            self._rest_hours += rest_hours

    def start_returning_home(self):
        self._destination = self._home_name
        self._hours_since_rest = 0

    def reset_after_return(self):
        self._destination = None
        self._distance = 0
        self._hours_since_rest = None
        self._rest_hours = None

    def __str__(self):
        destination = self._destination
        distance = self._distance
        hours_since_rest = self._hours_since_rest
        rest_hours = self._hours_since_rest
        return (
            f"Destination: {destination}\n"
            f"Distance: {distance}\n"
            f"Hours since rest: {hours_since_rest}\n"
            f"Rest hours: {rest_hours}"
        )
