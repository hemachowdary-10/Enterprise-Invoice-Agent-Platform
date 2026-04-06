from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest()

def detect(invoice):

    amount = np.array([[float(invoice.get("total",0))]])

    score = model.predict(amount)

    if score[0] == -1:
        return "fraud_suspected"

    return "clear"