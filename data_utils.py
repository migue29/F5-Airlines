from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pandas as pd
from pandasgui import show


def preprocess_numeric(X):
    """
    The function preprocess_numeric takes a DataFrame X, selects the numeric columns, and applies
    imputation and scaling to those columns.

    :param X: X is a pandas DataFrame containing the numeric features that need to be preprocessed
    :return: two values: `numeric_cols` and `numeric_transformer`.
    """
    numeric_cols = X.select_dtypes(include=["number"]).columns
    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="mean")), ("scaler", MinMaxScaler())]
    )
    return numeric_cols, numeric_transformer


def preprocess_categorical(X):
    """
    The function preprocess_categorical takes a DataFrame X as input, identifies the categorical columns
    in X, and returns the categorical column names and a transformer object that imputes missing values
    with the most frequent value and encodes the categorical variables using one-hot encoding.

    :param X: The parameter X is a pandas DataFrame that contains the categorical columns that need to
    be preprocessed
    :return: two values: categorical_cols and categorical_transformer.
    """
    categorical_cols = X.select_dtypes(include=["object"]).columns
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(drop="if_binary", handle_unknown="ignore")),
        ]
    )
    return categorical_cols, categorical_transformer


def preprocess_data(X):
    """
    The function preprocess_data takes in a dataset X and applies preprocessing steps to both numeric
    and categorical columns.

    :param X: The parameter X represents the input data that needs to be preprocessed. It is assumed to
    be a pandas DataFrame or a numpy array
    :return: The function `preprocess_data` returns a `preprocessor` object, which is a
    `ColumnTransformer` that applies the specified transformations to the numeric and categorical
    columns of the input data `X`.
    """
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
    """
    The function trains a random forest classifier model on preprocessed data.

    :param X: The parameter X represents the input features or independent variables of the dataset. It
    is a matrix or dataframe with shape (n_samples, n_features), where n_samples is the number of
    samples or observations and n_features is the number of features or variables
    :param y: The parameter "y" represents the target variable or the labels of the data. It is a
    one-dimensional array or list that contains the true values corresponding to each data point in X.
    The length of "y" should be equal to the number of rows or instances in X
    :return: two objects: the trained RandomForestClassifier model (clf) and the preprocessor object.
    """
    # Preprocesar los datos
    preprocessor = preprocess_data(X)
    X_preprocessed = preprocessor.fit_transform(X)
    # Entrenar el modelo
    clf = RandomForestClassifier()
    clf.fit(X_preprocessed, y)

    return clf, preprocessor
