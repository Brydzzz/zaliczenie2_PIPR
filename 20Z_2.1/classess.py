class NoBedsError(Exception):
    def __init__(self):
        super().__init__("There are no available beds")


class Hospital:
    def __init__(
        self,
        town: str,
        covid_beds: int,
        covid_oiom_beds: int,
        no_covid_beds: int,
        no_covid_oiom_beds: int,
    ):
        self._town = town
        self._covid_beds = covid_beds
        self._covid_oiom_beds = covid_oiom_beds
        self._no_covid_beds = no_covid_beds
        self._no_covid_oiom_beds = no_covid_oiom_beds

    @property
    def town(self):
        return self._town

    @property
    def covid_beds(self):
        return self._covid_beds

    @property
    def covid_oiom_beds(self):
        return self._covid_oiom_beds

    @property
    def no_covid_beds(self):
        return self._no_covid_beds

    @property
    def no_covid_oiom_beds(self):
        return self._no_covid_oiom_beds


class Patient:
    def __init__(self, town, if_covid: 1, if_critical: 0):
        self._town = town
        if town == "Warszawa":
            self._nearest_hospitals = ["Warszawa", "Siedlce", "Radom"]
        elif town == "Siedlce":
            self._nearest_hospitals = ["Siedlce", "Warszawa", "Radom"]
        else:
            self._nearest_hospitals = ["Radom", "Warszawa", "Siedlce"]
        self._if_covid = if_covid
        self._if_critical = if_critical

    @property
    def town(self):
        return self._town

    @property
    def if_covid(self):
        return self._if_covid

    @property
    def if_critical(self):
        return self._if_critical

    @property
    def nearest_hospitals(self):
        return self._nearest_hospitals

    def check_bed_availability(self, hospital: Hospital):
        patient_is_covid = self.if_covid
        patient_is_critical = self.if_critical
        if patient_is_covid and patient_is_critical:
            return hospital.covid_oiom_beds > 0
        elif patient_is_covid and not patient_is_critical:
            return hospital.covid_beds > 0
        elif not patient_is_covid and not patient_is_critical:
            return hospital.no_covid_beds > 0
        else:
            return hospital.no_covid_oiom_beds > 0

    def choose_hospital(self, hospital_list):
        nearest_hospital_list = self.nearest_hospitals
        for hospital_town in nearest_hospital_list:
            for hospital in hospital_list:
                if hospital_town == hospital.town:
                    if self.check_bed_availability(hospital):
                        return hospital.town
        raise NoBedsError
