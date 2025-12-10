import requests
import json

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


customer = {
  "customer": {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 100,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
  }
}
# set up "tenure": 100, ... to 10 or originally 1 - to get churn = True
result = requests.post(url, json=customer).json()
print(result)