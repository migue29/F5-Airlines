from pandasgui import show
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


def convert_objetive_bool(df):
    df.loc[df["satisfaction"] == "satisfied", "satisfaction"] = True
    df.loc[df["satisfaction"] == "neutral or dissatisfied", "satisfaction"] = False
    return df


def delete_columns(df):
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop("id", axis=1, inplace=True)
    return df


def impute_null(df):
    df["Arrival Delay in Minutes"].fillna(
        df["Arrival Delay in Minutes"].median(axis=0), inplace=True
    )


def scaler_encoder(df):
    categoricas = [
        "Gender",
        "Customer Type",
        "Type of Travel",
        "Class",
        "satisfaction",
        "Inflight wifi service",
        "Departure/Arrival time convenient",
        "Ease of Online booking",
        "Gate location",
        "Food and drink",
        "Online boarding",
        "Inflight entertainment",
        "On-board service",
        "Leg room service",
        "Baggage handling",
        "Checkin service",
        "Inflight service",
        "Cleanliness",
    ]
    categoricas_one = [
        "Gender",
        "Customer Type",
        "Type of Travel",
        "Class",
        "satisfaction",
    ]
    encoder = OneHotEncoder(sparse_output=False)
    dfCodificador = encoder.fit_transform(df[categoricas_one])
    columnasNuevas = encoder.get_feature_names_out(categoricas_one)
    dfcodificado = pd.DataFrame(dfCodificador, columns=columnasNuevas)

    # Concatenar el DataFrame codificado con el original
    df = pd.concat([df, dfcodificado], axis=1)

    # Eliminar las columnas originales
    df.drop(categoricas_one, axis=1, inplace=True)

    columns_to_scale = [
        "Age",
        "Flight Distance",
        "Departure Delay in Minutes",
        "Arrival Delay in Minutes",
    ]

    scaler = MinMaxScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    return df


def train_model(df):
    X = df.drop("Satisfied", axis=1)
    y = df["Satisfied"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.20, random_state=42
    )
    classifier = RandomForestClassifier(n_estimators=3)
    classifier.fit(X_train, y_train)
    return classifier


# todas las funciones
def preprocess_data(df):
    impute_null(df)
    convert_objetive_bool(df)
    df = delete_columns(df)
    df = scaler_encoder(df)
    df = df.drop(
        [
            "satisfaction_False",
            "Type of Travel_Personal Travel",
            "Gender_Male",
            "Customer Type_disloyal Customer",
        ],
        axis=1,
    )
    df = df.rename(
        columns={
            "satisfaction_True": "Satisfied",
            "Type of Travel_Business travel": "Business travel",
            "Gender_Female": "Gender",
            "Customer Type_Loyal Customer": "Loyal Customer",
        }
    )
    return df
