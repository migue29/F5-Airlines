from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def impute_numeric_data(data, strategy="mean"):
    imputer = SimpleImputer(strategy=strategy)
    return imputer.fit_transform(data)


def preprocess_data(X, numerical_cols, categorical_cols):
    numerical_transformer = Pipeline(steps=[("scaler", MinMaxScaler())])
    categorical_transformer = Pipeline(
        steps=[
            (
                "onehot",
                OneHotEncoder(drop="if_binary", handle_unknown="ignore", sparse=False),
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_cols),
            ("cat", categorical_transformer, categorical_cols),
        ],
        remainder="passthrough",
    )

    return preprocessor.fit_transform(X)
