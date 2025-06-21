import shap
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Use shap.Explainer instead of TreeExplainer for compatibility
explainer = shap.Explainer(model.predict, X_train)

# Get SHAP values
shap_values = explainer(X_test)

# Plot summary for all classes together
shap.plots.beeswarm(shap_values)
