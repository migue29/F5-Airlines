import streamlit as st
import pandas as pd

# Crear un DataFrame para almacenar los registros
df_registros = pd.DataFrame(
    columns=[
        "Gender",
        "Customer Type",
        "Age",
        "Type of Travel",
        "Class",
        "Flight distance",
        "Inflight wifi service",
        "Departure/Arrival time convenient",
        "Ease of Online booking",
        "Gate location",
    ]
)


# Título del formulario
st.title("Formulario de Retroalimentación de Pasajeros")

# Campo de opción para "Gender"
gender = st.radio("Gender", ("Female", "Male"))

# Campo de selección para "Customer Type"
customer_type = st.selectbox("Customer Type", ("Loyal customer", "Disloyal customer"))

# Campo de selección para "Age"
age = st.number_input("Age", min_value=0, max_value=120)

# Campo de selección para "Type of Travel"
travel_type = st.selectbox("Type of Travel", ("Personal Travel", "Business Travel"))

# Campo de selección para "Class"
travel_class = st.selectbox("Class", ("Business", "Eco", "Eco Plus"))

# Campo de texto para "Flight distance"
flight_distance = st.number_input("Flight distance", min_value=0)

# Campos de opción para satisfacción
inflight_wifi = st.radio(
    "Inflight wifi service", ("Not Applicable", "1", "2", "3", "4", "5")
)
departure_arrival = st.radio(
    "Departure/Arrival time convenient", ("Not Applicable", "1", "2", "3", "4", "5")
)
online_booking = st.radio(
    "Ease of Online booking", ("Not Applicable", "1", "2", "3", "4", "5")
)
gate_location = st.radio("Gate location", ("Not Applicable", "1", "2", "3", "4", "5"))

# Botón para enviar el formulario
submit_button = st.button("Enviar")

# Procesamiento de datos cuando se envía el formulario
if submit_button:
    # Agregar los datos ingresados al DataFrame de registros
    nuevo_registro = {
        "Gender": [gender],
        "Customer Type": [customer_type],
        "Age": [age],
        "Type of Travel": [travel_type],
        "Class": [travel_class],
        "Flight distance": [flight_distance],
        "Inflight wifi service": [inflight_wifi],
        "Departure/Arrival time convenient": [departure_arrival],
        "Ease of Online booking": [online_booking],
        "Gate location": [gate_location],
    }

    df_nuevo_registro = pd.DataFrame(nuevo_registro)
    df_registros = pd.concat([df_registros, df_nuevo_registro], ignore_index=True)

    # Mostrar el DataFrame con el registro ingresado
    st.subheader("Registro ingresado:")
    st.write(df_registros.tail(1))  # Mostrar el último registro ingresado

    # Limpiar el formulario después de enviarlo
    st.success("¡Formulario enviado con éxito!")
    gender = None
    customer_type = None
    age = None
    travel_type = None
    travel_class = None
    flight_distance = None
    inflight_wifi = None
    departure_arrival = None
    online_booking = None
    gate_location = None
