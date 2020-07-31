import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# read in the model
my_model = pickle.load(open("logit_pickled.p", "rb"))
scaler = pickle.load(open("scaler.p", "rb"))

# create a function to take in user-entered amounts and apply the model
def benign_malignant(amounts_float, model=my_model):
    # scale the user inputs
    amounts_scaled = scaler.transform(amounts_float)

    # inputs into the model
    input_df = amounts_scaled

    # make a prediction
    prediction = my_model.predict(input_df)[0]

    # return a message
    message_array = ["Benign Tumor", "Malignant Tumor"]

    return message_array[prediction]
