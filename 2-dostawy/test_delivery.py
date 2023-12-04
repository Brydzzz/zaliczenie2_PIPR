from delivery import (
    Delivery,
    DestinationAlreadySet,
    DestinationNotInOffer,
    DriverIsResting,
    RideTooLong,
)
from pytest import raises


def test_create_delivery():
    delivery = Delivery(13, "Gdańsk", 1, None)
    assert delivery.distance == 13
    assert delivery.destination == "Gdańsk"
    assert delivery.hours_since_rest == 1
    assert delivery.rest_hours is None


def test_create_empty_delivery():
    delivery = Delivery()
    assert delivery.distance == 0
    assert delivery.destination is None
    assert delivery.hours_since_rest is None
    assert delivery.rest_hours is None


def test_submit_order_typical():
    delivery = Delivery()
    assert delivery.distance == 0
    assert delivery.destination is None
    assert delivery.hours_since_rest is None
    assert delivery.rest_hours is None
    delivery.submit_order("Kraków")
    assert delivery.destination == "Kraków"
    assert delivery.distance == 290
    assert delivery.hours_since_rest == 0
    assert delivery.rest_hours is None


def test_submit_order_destination_already_set():
    delivery = Delivery(13, "Gdańsk", 1, None)
    with raises(DestinationAlreadySet):
        delivery.submit_order("Poznań")


def test_submit_order_destination_not_in_offer():
    delivery = Delivery()
    with raises(DestinationNotInOffer):
        delivery.submit_order("Sochaczew")


def test_drive_typical():
    delivery = Delivery(290, "Kraków", 0)
    delivery.drive(3)
    assert delivery.distance == 50
    assert delivery.hours_since_rest == 3


def test_drive_arrived_at_destination():
    delivery = Delivery(240, "Kraków", 0)
    delivery.drive(3)
    assert delivery.destination == "Warszawa"
    assert delivery.hours_since_rest == 0
    assert delivery.distance == 290


def test_drive_arrived_home():
    delivery = Delivery(240, "Warszawa", 0)
    delivery.drive(3)
    assert delivery.distance == 0
    assert delivery.destination is None
    assert delivery.hours_since_rest is None
    assert delivery.rest_hours is None


def test_drive_driver_is_resting():
    delivery = Delivery(240, "Warszawa", None, 1)
    with raises(DriverIsResting):
        delivery.drive(2)


def test_drive_driver_rested_enough():
    delivery = Delivery(240, "Warszawa", 0, 5)
    delivery.drive(2)
    assert delivery.distance == 80
    assert delivery.destination == "Warszawa"
    assert delivery.hours_since_rest == 2
    assert delivery.rest_hours is None


def test_drive_ride_too_long():
    delivery = Delivery(240, "Warszawa", 2)
    with raises(RideTooLong):
        delivery.drive(2)


def test_start_returning_home():
    delivery = Delivery(240, "Kraków", 0)
    delivery.start_returning_home()
    assert delivery.destination == "Warszawa"
    assert delivery.hours_since_rest == 0
    assert delivery.distance == 290


def test_reset_after_return():
    delivery = Delivery(240, "Warszawa", 0)
    delivery.reset_after_return()
    assert delivery.distance == 0
    assert delivery.destination is None
    assert delivery.hours_since_rest is None
    assert delivery.rest_hours is None


def test_delivery_to_text():
    delivery = Delivery(240, "Warszawa", 2)
    assert str(delivery) == (
        "Destination: Warszawa\n"
        "Distance: 240 km\n"
        "Hours since rest: 2 h\n"
        "Rest hours: Unknown h"
    )


def test_delivery_to_text_empty_delivery():
    delivery = Delivery()
    assert str(delivery) == (
        "Destination: Not Set\n"
        "Distance: 0 km\n"
        "Hours since rest: Unknown h\n"
        "Rest hours: Unknown h"
    )
