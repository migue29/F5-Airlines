import pandas as pd
from data_utils import (
    get_categorical_cols,
    get_imputer_cols,
    load_data,
    select_first_record,
    fill_null_with_mode,
)
from preprocessing import impute_numeric_data, preprocess_data
from model import split_data, train_random_forest, cross_val_predict_proba
from evaluation import calculate_average_probability
import os

os.system("cls")
# Carga de datos
# python initial.py
train_data = load_data("data/airline_passenger_satisfaction.csv")
primer_registro = select_first_record(train_data)
test_data = pd.DataFrame([primer_registro])


# Llenar valores nulos
imputer_cols = get_imputer_cols(train_data)
fill_null_with_mode(imputer_cols, train_data, test_data)
categorical_cols = get_categorical_cols(train_data)

print("*" * 50)
impute_numeric_data(train_data, "mean")

# División de datos
X_train, X_test, y_train, y_test = split_data(X, y)

# Entrenamiento del modelo
classifier = train_random_forest(X_train, y_train)

# Validación cruzada y cálculo de probabilidad promedio
proba_predictions = cross_val_predict_proba(classifier, X, y, cv=10)
average_prob = calculate_average_probability(proba_predictions)

print("Average probability:", average_prob)
