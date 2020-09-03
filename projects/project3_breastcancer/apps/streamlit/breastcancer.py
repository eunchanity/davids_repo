import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# read in the model
my_model = pickle.load(open("pickle/logit_pickled.p", "rb"))
scaler = pickle.load(open("pickle/scaler.p", "rb"))

# streamlit beta styling
st.beta_set_page_config(
    page_title="Breast Cancer Tumor Classifier",
    page_icon=":clipboard:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
# streamlit outline
st.title("Breast Cancer Tumor Classifier")
st.markdown("---")
# display of popularity meter and number
status_text = st.text("The tumor is determined to be a:")
diagnosis_display = st.empty()

st.markdown("---")
st.subheader("Adjust the Values to Check the Diagnosis:")
st.text("")

clumpthickness = st.slider(
    "Clump Thickness", min_value=0, max_value=10, value=2, step=1
)
cellsize = st.slider(
    "Uniformity of Cell Size", min_value=0, max_value=10, value=2, step=1
)
margadhesion = st.slider(
    "Marginal Adhesion", min_value=0, max_value=10, value=2, step=1
)
epithelial = st.slider(
    "Single Epithelial Cell Size", min_value=0, max_value=10, value=2, step=1
)
barenuclei = st.slider("Bare Nuclei", min_value=0, max_value=10, value=2, step=1)
blandchromatin = st.slider(
    "Bland Chromatin", min_value=0, max_value=10, value=2, step=1
)
nucleoli = st.slider("Normal Nucleoli", min_value=0, max_value=10, value=2, step=1)
mitoses = st.slider("Mitoses", min_value=0, max_value=10, value=2, step=1)

st.markdown("---")

# user inputs for cell characteristics
amounts = [
    clumpthickness,
    cellsize,
    margadhesion,
    epithelial,
    epithelial,
    blandchromatin,
    nucleoli,
    mitoses,
]

# predict benign/malignant
def benign_malignant(amounts, model=my_model):
    """
    input: takes in user input from slider widgets
    output: classification of tumor as either benign or malignant
    """
    # scale the user inputs
    amounts_scaled = scaler.transform(amounts)
    # inputs into the model
    input_df = amounts_scaled
    # make a prediction
    prediction = my_model.predict(input_df)[0]
    # return a message
    message_array = ["Benign Tumor", "Malignant Tumor"]
    return message_array[prediction]


final_message = benign_malignant(np.array(amounts).reshape(1, -1))
diagnosis_display.markdown(f"**{final_message}**")

# sidebar
st.sidebar.title("About This App")
st.sidebar.markdown(
    "This app predicts whether or not a tumor is benign or malignant based on its cell characteristics.  \n"
    "  \n"
    "Each of the characteristics are measured on a scale from 1-10 as defined by the Wisconsin Breast Cancer study. "
)
st.sidebar.markdown("---")
st.sidebar.subheader("Technical Details")
st.sidebar.markdown(
    "A logistic regression model was selected and trained on cell characteristics defined below.  \n"
    "  \n"
    "The ROC/AUC score was `0.99` and the F1 score was `0.98`.  \n"
    "  \n"
    "_Read the in-depth analysis in my [blog post](https://eunchanity.github.io/breast-cancer/)_"
)
st.sidebar.subheader("Terminology")
st.sidebar.markdown(
    "  \n"
    "**Clump Thickness**: assesses if cells are mono- or multi-layered  \n"
    "**Uniformity of Cell Size**: evaluates the consistency in size of cells in sample  \n"
    "**Marginal Adhesion**: quantifies how much cells on the outside of the epithelial tend to stick together  \n"
    "**Single Epithelial Cell Size**: relates to cell uniformity, determines if epithelial cells are significantly enlarged  \n"
    "**Bare Nuclei**: calculates the proportion of the number of cells not surrounded by cytoplasm to those that are  \n"
    "**Bland Chromatin**: rates the uniform “texture” of the nucleus in a range from fine to coarse  \n"
    "**Normal Nucleoli**: determines whether the nucleoli are small and barely visible or larger, more visible, and more plentiful  \n"
    "**Mitoses**: describes the level of mitotic (cell reproduction) activity"
)

st.sidebar.subheader("References")
st.sidebar.markdown(
    "Dataset Used: [Breast Cancer Wisconsin (Original) Data Set](hhttps://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original))"
)
st.sidebar.markdown("---")

st.sidebar.markdown("**Created by David Weon**")
st.sidebar.markdown(
    "[Link to App Github](https://github.com/eunchanity/breast_cancer_classifier)  \n"
    "[Link to Blog Post](https://eunchanity.github.io/breast-cancer/)"
)
