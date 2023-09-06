from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import cross_val_predict


def split_data(X, y, random_state=0):
    return train_test_split(
        X, y, stratify=y, train_size=0.8, test_size=0.2, random_state=random_state
    )


def train_random_forest(X_train, y_train, n_estimators=3):
    classifier = RandomForestClassifier(n_estimators=n_estimators)
    classifier.fit(X_train, y_train)
    return classifier


def cross_val_predict_proba(model, X, y, cv=10):
    return cross_val_predict(model, X, y, cv=cv, method="predict_proba")
