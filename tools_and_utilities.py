import streamlit as st


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


def create_passenger_satisfaction_form():
    data = {
        "Unnamed: 0": 0,
        "id": 0,
        "satisfaction": "nada",
    }

    data["id"] = st.number_input("ID")
    data["Gender"] = st.selectbox("Gender", ["Female", "Male"])
    data["Customer Type"] = st.selectbox(
        "Customer Type", ["Loyal customer", "disloyal customer"]
    )
    data["Age"] = st.number_input(
        "Age", min_value=7, max_value=80, value=7, step=1, format="%d"
    )
    data["Type of Travel"] = st.selectbox(
        "Type of Travel", ["Personal Travel", "Business Travel"]
    )
    data["Class"] = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])
    data["Flight Distance"] = st.number_input(
        "Flight Distance", min_value=31, max_value=4982, value=31, step=1, format="%d"
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
        "Checkin service",
        "Inflight service",
        "Cleanliness",
    ]

    for column in satisfaction_columns:
        data[column] = st.slider(column, min_value=0, max_value=5, key=column)

    data["Departure Delay in Minutes"] = st.number_input(
        "Departure Delay in Minutes", step=1, key="departure_delay"
    )
    data["Arrival Delay in Minutes"] = st.number_input(
        "Arrival Delay in Minutes", step=1, key="arrival_delay"
    )

    return data
