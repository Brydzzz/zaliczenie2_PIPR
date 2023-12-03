from classess import Hospital, Patient


def test_create_hospital():
    hospital = Hospital("Warszawa", 1800, 400, 2200, 200)
    assert hospital.town == "Warszawa"
    assert hospital.covid_beds == 1800
    assert hospital.covid_oiom_beds == 400
    assert hospital.no_covid_beds == 2200
    assert hospital._no_covid_oiom_beds == 200


def test_create_patient():
    patient = Patient("Warszawa", True, False)
    assert patient.town == "Warszawa"
    assert patient.if_covid is True
    assert patient.if_critical is False


# pewnie wypadałoby dopisać resztę testów
