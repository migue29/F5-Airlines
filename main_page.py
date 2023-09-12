import pickle
import streamlit as st
import pandas as pd
from tools_and_utilities import (
    validate_age,
    validate_flight_distance,
    validate_delay,
    create_passenger_satisfaction_form,
)
import os
from database import connect_to_mongodb

os.system("cls")
st.title("Formulario de Satisfacción del Pasajero")

# The `create_passenger_satisfaction_form()` function is creating a dictionary that represents a form
# for collecting passenger satisfaction data. This form includes fields such as age, flight distance,
# departure delay, and arrival delay. The function returns this dictionary, which is stored in the
# `form_data` variable.

form_data = create_passenger_satisfaction_form()


if st.button("Enviar"):
    # This `if` statement is checking if the values entered in the form for age, flight distance,
    # departure delay, and arrival delay are valid. It does this by calling the respective validation
    # functions (`validate_age`, `validate_flight_distance`, `validate_delay`) and passing the
    # corresponding form data as arguments.
    if (
        validate_age(form_data["Age"])
        and validate_flight_distance(form_data["Flight Distance"])
        and validate_delay(form_data["Departure Delay in Minutes"])
        and validate_delay(form_data["Arrival Delay in Minutes"])
    ):
        test_data = pd.DataFrame([form_data])

        with open("model.pkl", "rb") as model_file:
            model = pickle.load(model_file)

        with open("preprocessor.pkl", "rb") as preprocessor_file:
            preprocessor = pickle.load(preprocessor_file)

        # para probarlo con 100 registros ojo hay que descomentar donde test data obtiene los datos de form_data
        # train_data = pd.read_csv("data/airline_passenger_satisfaction.csv")
        # primeros_100_registros = train_data.iloc[0:100]
        # test_data = pd.DataFrame(primeros_100_registros)
        # test_data.drop(["satisfaction", "Unnamed: 0", "id"], axis=1, inplace=True)

        X_test_data_preprocessed = preprocessor.transform(test_data)

        predictions = model.predict(X_test_data_preprocessed)
        st.info(
            f"Nuestra aplicacion ha analizado que usted se encuentra: {predictions}, con nuestro servicio"
        )

        db = connect_to_mongodb()
        if db is None:
            st.error(
                "No se pudo conectar a la base de datos. Verifica la configuración de MongoDB."
            )
        else:
            collection = db["satisfaction_users"]
            collection.insert_one(form_data)
