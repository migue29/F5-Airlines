import streamlit as st
import pandas as pd
from tools_and_utilities import (
    validate_age,
    validate_flight_distance,
    validate_delay,
    create_passenger_satisfaction_form,
)
import os

os.system("cls")
st.title("Formulario de Satisfacción del Pasajero")

form_data = create_passenger_satisfaction_form()

if st.button("Enviar"):
    if (
        validate_age(form_data["Age"])
        and validate_flight_distance(form_data["Flight distance"])
        and validate_delay(form_data["Departure Delay in Minutes"])
        and validate_delay(form_data["Arrival Delay in Minutes"])
    ):
        test_data = pd.DataFrame([form_data])
        st.subheader("Último registro agregado:")
        st.write(test_data.tail(1))
        print(form_data)
