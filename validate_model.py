import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Load or train a simple model
model = RandomForestClassifier()
model.fit(X, y)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Test script
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Test predictions
predictions = model.predict(X)
results = []
for i, (pred, actual) in enumerate(zip(predictions, y)):
    status = "Pass" if pred == actual else "Fail"
    results.append([i, pred, actual, status])

# Save results
df = pd.DataFrame(results, columns=["Test_ID", "Predicted", "Actual", "Status"])
df.to_csv("test_results.csv", index=False)

# Summary
accuracy = (df["Status"] == "Pass").mean()
print(f"Accuracy: {accuracy*100:.2f}%")
with open("summary.txt", "w") as f:
    f.write(f"Total Tests: {len(df)}\nPassed: {(df['Status'] == 'Pass').sum()}\nAccuracy: {accuracy*100:.2f}%")