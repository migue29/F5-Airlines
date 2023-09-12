import pandas as pd
import warnings
from pandasgui import show
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data_utils import train_model
import pickle

train_data = pd.read_csv("data/airline_passenger_satisfaction.csv")
df = pd.DataFrame(train_data)
X = df.drop(["satisfaction", "Unnamed: 0" , "id"], axis=1)
y = df["satisfaction"]
# Entrenar el modelo
model, preprocessor = train_model(X, y)

# Guardar el modelo en un archivo pickle
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# Guardar el preprocesador en un archivo pickle
with open("preprocessor.pkl", "wb") as preprocessor_file:
    pickle.dump(preprocessor, preprocessor_file)
