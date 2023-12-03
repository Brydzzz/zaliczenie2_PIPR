from delivery import (
    Delivery,
    # DestinationAlreadySet,
    # DestinationNotInOffer,
    # DriverIsResting,
    # RideTooLong,
)


def test_create_delivery():
    delivery = Delivery(13, "Gdańsk", 1, None)
    assert delivery.distance == 13
