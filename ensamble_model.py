# Este código seria útil para entrenar el modelo con técnicas ensamble (StackingClassifier)

class ModelStacking:
    def __init__(self, X, y, meta_classifier=None):
        self.X = X
        self.y = y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, stratify=y, train_size=0.8, test_size=0.2, random_state=0)
        self.random_forest = RandomForestClassifier(n_estimators=50)
        self.adaboost = AdaBoostClassifier(n_estimators=50)
        self.gradient_boosting = GradientBoostingClassifier(n_estimators=50)
        self.meta_classifier = meta_classifier if meta_classifier else RandomForestClassifier(n_estimators=50)
        self.stacking_model = None
    
    def train_stacking_model(self):
        models = [
            ('random_forest', self.random_forest),
            ('adaboost', self.adaboost),
            ('gradient_boosting', self.gradient_boosting)
        ]
        
        self.stacking_model = StackingClassifier(estimators=models, final_estimator=self.meta_classifier)
        self.stacking_model.fit(self.X_train, self.y_train)
    
    def evaluate_stacking_model(self):
        if self.stacking_model:
            y_pred = self.stacking_model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            conf_matrix = confusion_matrix(self.y_test, y_pred)
            precision = precision_score(self.y_test, y_pred, average='macro')
            recall = recall_score(self.y_test, y_pred, average='macro')
            f1 = f1_score(self.y_test, y_pred, average='macro')
            
            print("Accuracy:", accuracy)
            print("Matriz de Confusión:\n", conf_matrix)
            print("Precisión (Macro):", precision)
            print("Recall (Macro):", recall)
            print("F1-Score (Macro):", f1)
        else:
            print("Entrena el modelo de stacking primero.")


if __name__ == "__main__":
    model_stacking = ModelStacking(X_train, y_train)  
    model_stacking.train_stacking_model()
    model_stacking.evaluate_stacking_model()