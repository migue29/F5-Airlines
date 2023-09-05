import streamlit as st
import pandas as pd
import sys
import os
from pandasgui import show
import warnings

warnings.filterwarnings("ignore")
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ruta_proyecto, ".."))


# Función para validar los campos de entrada
def validate_age(age):
    if age < 7 or age > 80:
        st.error("La edad debe estar entre 7 y 80.")
        return False
    return True


def validate_flight_distance(distance):
    if distance < 31 or distance > 4982:
        st.error("La distancia de vuelo debe estar entre 31 y 4982.")
        return False
    return True


def validate_delay(minutes):
    if not isinstance(minutes, int):
        st.error("El valor debe ser un número entero.")
        return False
    return True


# Crear el formulario
st.title("Formulario de Satisfacción del Pasajero")

id = st.number_input("ID")
gender = st.selectbox("Gender", ["Female", "Male"])
customer_type = st.selectbox("Customer Type", ["Loyal customer", "disloyal customer"])
age = st.number_input(
    "Age", min_value=7, max_value=80, value=7, step=1, format="%d", key="age"
)
type_of_travel = st.selectbox("Type of Travel", ["Personal Travel", "Business Travel"])
travel_class = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])
flight_distance = st.number_input(
    "Flight distance",
    min_value=31,
    max_value=4982,
    value=31,
    step=1,
    format="%d",
    key="flight_distance",
)

satisfaction_columns = [
    "Inflight wifi service",
    "Departure/Arrival time convenient",
    "Ease of Online booking",
    "Gate location",
    "Food and drink",
    "Online boarding",
    "Seat comfort",
    "Inflight entertainment",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Check-in service",
    "Inflight service",
    "Cleanliness",
]

satisfaction_ratings = {}
for column in satisfaction_columns:
    satisfaction_ratings[column] = st.slider(
        column, min_value=0, max_value=5, key=column
    )

departure_delay = st.number_input(
    "Departure Delay in Minutes", step=1, key="departure_delay"
)
arrival_delay = st.number_input("Arrival Delay in Minutes", step=1, key="arrival_delay")

# Botones para enviar y limpiar el formulario
if st.button("Enviar"):
    if (
        validate_age(age)
        and validate_flight_distance(flight_distance)
        and validate_delay(departure_delay)
        and validate_delay(arrival_delay)
    ):
        data = {
            "Unnamed: 0": 00,
            "id": 00,
            "Gender": gender,
            "Customer Type": customer_type,
            "Age": age,
            "Type of Travel": type_of_travel,
            "Class": travel_class,
            "Flight distance": flight_distance,
            **satisfaction_ratings,
            "Departure Delay in Minutes": departure_delay,
            "Arrival Delay in Minutes": arrival_delay,
            "satisfaction": "nada",
        }
        test_data = pd.DataFrame([data])
# Mostrar el DataFrame actualizado
st.subheader("Último registro agregado:")
# st.write(test_data.tail(1))
