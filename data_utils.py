from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pandas as pd


def preprocess_numeric(X):
    numeric_cols = X.select_dtypes(include=["number"]).columns
    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="mean")), ("scaler", MinMaxScaler())]
    )
    return numeric_cols, numeric_transformer


def preprocess_categorical(X):
    categorical_cols = X.select_dtypes(include=["object"]).columns
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(drop="if_binary", handle_unknown="ignore")),
        ]
    )
    return categorical_cols, categorical_transformer


def preprocess_data(X):
    numeric_cols, numeric_transformer = preprocess_numeric(X)
    categorical_cols, categorical_transformer = preprocess_categorical(X)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols),
        ]
    )

    return preprocessor


def train_model(X, y):
    # Preprocesar los datos
    preprocessor = preprocess_data(X)
    X_preprocessed = preprocessor.fit_transform(X)

    # Entrenar el modelo
    clf = RandomForestClassifier()
    clf.fit(X_preprocessed, y)

    return clf, preprocessor
