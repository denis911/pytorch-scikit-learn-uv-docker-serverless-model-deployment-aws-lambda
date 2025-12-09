import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)

# # dummy version
# def predict_single(customer):
#     # we will put our model here
#     return 0.56

def lambda_handler(event, context):    
    print("Parameters:", event)
    customer = event['customer']
    prob = predict_single(customer)
    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }

# real vs dummy prediction function which predicts churn for all inputs

