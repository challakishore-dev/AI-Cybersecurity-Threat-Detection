
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib, os
import matplotlib.pyplot as plt

os.makedirs("models", exist_ok=True)
os.makedirs("images", exist_ok=True)

data = pd.read_csv("data/data.csv")

X = data.drop("Attack_Label", axis=1)
y = data["Attack_Label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier(n_estimators=150)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("\nREPORT:\n")
print(classification_report(y_test,y_pred))

# confusion matrix
cm = confusion_matrix(y_test,y_pred)
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.savefig("images/confusion_matrix.png")

joblib.dump(model,"models/model.pkl")

print("\nSaved model + confusion matrix")
