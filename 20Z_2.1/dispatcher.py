from classess import Hospital, Patient

hospital_warszawa = Hospital("Warszawa", 1800, 400, 2200, 200)
hospital_siedlce = Hospital("Siedlce", 335, 110, 455, 40)
hospital_radom = Hospital("Radom", 300, 90, 200, 25)
hospital_list = [hospital_warszawa, hospital_siedlce, hospital_radom]

# def choose_hospital(patient: Patient):
#     nearest_hospital_list = patient.nearest_hospitals
#     for hospital in nearest_hospital_list:
#         if check_bed_availability:
#             return hospital
#     raise NoBedsError


# def check_bed_availability(hospital: Hospital, patient: Patient):
#     patient_is_covid = patient.if_covid
#     patient_is_critical = patient.if_critical
#     if patient_is_covid and patient_is_critical:
#         return hospital.covid_oiom_beds > 0
#     elif patient_is_covid and not patient_is_critical:
#         return hospital.covid_beds > 0
#     elif not patient_is_covid and not patient_is_critical:
#         return hospital.no_covid_beds > 0
#     else:
#         return hospital.no_covid_oiom_beds > 0


if __name__ == "__main__":
    patient = Patient("Warszawa", True, False)
    print(patient.choose_hospital(hospital_list))
