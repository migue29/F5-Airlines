import pickle
import streamlit as st
import pandas as pd
from main import prediction_model
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
        and validate_flight_distance(form_data["Flight Distance"])
        and validate_delay(form_data["Departure Delay in Minutes"])
        and validate_delay(form_data["Arrival Delay in Minutes"])
    ):
        # test_data = pd.DataFrame([form_data])
        # st.subheader("Último registro agregado:")
        # st.write(test_data.tail(1))

        with open("model.pkl", "rb") as model_file:
            model = pickle.load(model_file)

        with open("preprocessor.pkl", "rb") as preprocessor_file:
            preprocessor = pickle.load(preprocessor_file)

        # para probarlo con 100 registros ojo hay que descomentar donde test data obtiene los datos de form_data
        train_data = pd.read_csv("data/airline_passenger_satisfaction.csv")
        primeros_100_registros = train_data.iloc[:100]
        test_data = pd.DataFrame(primeros_100_registros)
        test_data.drop(["satisfaction"], axis=1, inplace=True)
        #

        # ojo No se necesita la variable objetivo para la predicción
        X_test_data_preprocessed = preprocessor.transform(test_data)

        # Realizar la predicción
        predictions = model.predict(X_test_data_preprocessed)

        # Mostrar el resultado de la predicción
        print(predictions)

        st.write(f"El resultado es: {predictions}")
