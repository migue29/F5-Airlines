import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import warnings
from pandasgui import show
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import cross_val_predict
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)
warnings.filterwarnings("ignore")
train_data = pd.read_csv("data/airline_passenger_satisfaction.csv")  # ya
# primeros_100_registros = train_data.iloc[:100]
# test_data = pd.DataFrame(primeros_100_registros)
primer_registro = train_data.iloc[0]  # ya
test_data = pd.DataFrame([primer_registro])  # ya


# obtenemos un arreglo con los nombres de las variables segun su tipo
imputer_cols = [
    cname
    for cname in train_data.columns
    if train_data[cname].dtype in ["int64", "float64"]
]  # ya
categorical_cols = [
    cname for cname in train_data.columns if train_data[cname].dtype == "object"
]  # ya


imputer = SimpleImputer(strategy="mean")  # ya esta en la funcion
imputer.fit(train_data[imputer_cols])
train_data[imputer_cols] = imputer.transform(train_data[imputer_cols])
test_data[imputer_cols] = imputer.transform(test_data[imputer_cols])


# completamos valores nulos  en las columnas categoricas con la moda
def fill_null_with_mode(column, train_df, test_df):
    moda = train_df[column].mode().iloc[0]
    train_df[column] = train_df[column].fillna(moda)
    test_df[column] = test_df[column].fillna(moda)


# Aplicar la función de llenado de valores nulos
fill_null_with_mode(categorical_cols, train_data, test_data)


# preparamos los datos para dividirlos
train_data.drop(["Unnamed: 0", "id"], axis=1, inplace=True)
test_data.drop(["Unnamed: 0", "id", "satisfaction"], axis=1, inplace=True)
# TODO no estoy seguro si debo elimiar satisfaction de test
X = train_data.drop("satisfaction", axis=1)
y = train_data["satisfaction"]


# encoding y escaling

numerical_cols = [
    cname for cname in X.columns if X[cname].dtype in ["int64", "float64"]
]
print(numerical_cols)
categorical_cols = [cname for cname in X.columns if X[cname].dtype == "object"]
print(categorical_cols)
boolean_cols = [cname for cname in X.columns if X[cname].dtype == "bool"]
print(boolean_cols)

# Scale numerical data to have mean=0 and variance=1
numerical_transformer = Pipeline(steps=[("scaler", MinMaxScaler())])

# One-hot encode categorical data
categorical_transformer = Pipeline(
    steps=[
        (
            "onehot",
            OneHotEncoder(drop="if_binary", handle_unknown="ignore", sparse=False),
        )
    ]
)

# Combine preprocessing
ct = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_cols),
        ("cat", categorical_transformer, categorical_cols),
    ],
    remainder="passthrough",
)

# Apply preprocessing
X = ct.fit_transform(X)
test_data = ct.transform(test_data)

# Print new shape
print("Training set shape:", X.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, train_size=0.8, test_size=0.2, random_state=0
)


# Crear el pipeline con los parametros del grid research
# my_pipeline = Pipeline(steps=[
#     ('model', XGBClassifier(**clf_best_params["LGBM"], random_state=0))
# ])
my_pipeline = Pipeline(steps=[("model", RandomForestClassifier(n_estimators=3))])

# Realizar la validación cruzada y obtener las probabilidades y los scores
proba_predictions = cross_val_predict(my_pipeline, X, y, cv=10, method="predict_proba")
accuracy_scores = cross_val_predict(my_pipeline, X, y, cv=10, method="predict")

# Calcular promedio de las probabilidades de la clase positiva
preds = proba_predictions[:, 1].mean()

# Calcular promedio del score de precisión
# average_accuracy = accuracy_score(y, accuracy_scores)

# Imprimir los resultados
print("Average probability:", preds)
# print("Average accuracy:", average_accuracy)


classifier = RandomForestClassifier(n_estimators=3)
classifier.fit(X, y)
resultado = classifier.predict(test_data)
print(resultado)
