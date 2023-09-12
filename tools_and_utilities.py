import streamlit as st
import streamlit.components.v1 as components


def validate_age(age):
    """
    The function "validate_age" checks if an age is between 7 and 80, and returns True if it is, and
    False otherwise.

    :param age: The parameter "age" is the age value that needs to be validated
    :return: a boolean value. It returns True if the age is between 7 and 80, and False otherwise.
    """
    if age < 7 or age > 80:
        st.error("La edad debe estar entre 7 y 80.")
        return False
    return True


def validate_flight_distance(distance):
    """
    The function `validate_flight_distance` checks if a given flight distance is within the valid range
    of 31 to 4982.

    :param distance: The parameter "distance" represents the distance of a flight
    :return: a boolean value. If the distance is within the valid range (between 31 and 4982), the
    function will return True. Otherwise, it will return False.
    """
    if distance < 31 or distance > 4982:
        st.error("La distancia de vuelo debe estar entre 31 y 4982.")
        return False
    return True


def validate_delay(minutes):
    """
    The function "validate_delay" checks if the input is an integer and returns True if it is, otherwise
    it returns False and displays an error message.

    :param minutes: The parameter "minutes" is the value that needs to be validated. It should be an
    integer representing the number of minutes
    :return: a boolean value. It returns True if the input "minutes" is an integer, and False otherwise.
    """
    if not isinstance(minutes, int):
        st.error("El valor debe ser un número entero.")
        return False
    return True


def create_passenger_satisfaction_form():
    """
    The function `create_passenger_satisfaction_form` creates a form to collect data on passenger
    satisfaction.
    :return: The function `create_passenger_satisfaction_form` returns a dictionary `data` containing
    the passenger satisfaction form data.
    """
    data = {
        # "Unnamed: 0": 0,
        # "id": 0,
        # "satisfaction": "nada",
    }

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

    #  here is creating a set of radio buttons for each column in the
    # `satisfaction_columns` list. Each radio button represents a rating from 0 to 5 for a specific
    # aspect of passenger satisfaction.
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
        # data[column] = st.slider(column, min_value=0, max_value=5, key=column)  # slider
        data[column] = st.radio(
            column, options=list(range(6)), key=column, horizontal=True
        )

    data["Departure Delay in Minutes"] = st.number_input(
        "Departure Delay in Minutes", step=1, key="departure_delay"
    )
    data["Arrival Delay in Minutes"] = st.number_input(
        "Arrival Delay in Minutes", step=1, key="arrival_delay"
    )

    return data
