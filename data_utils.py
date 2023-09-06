import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def select_first_record(data):
    return data.iloc[0]


def get_imputer_cols(df):
    imputer_cols = [
        cname for cname in df.columns if df[cname].dtype in ["int64", "float64"]
    ]
    return imputer_cols


def get_categorical_cols(df):
    categorical_cols = [cname for cname in df.columns if df[cname].dtype == "object"]
    return categorical_cols


def fill_null_with_mode(column, train_df, test_df):
    moda = train_df[column].mode().iloc[0]
    train_df[column] = train_df[column].fillna(moda)
    test_df[column] = test_df[column].fillna(moda)
