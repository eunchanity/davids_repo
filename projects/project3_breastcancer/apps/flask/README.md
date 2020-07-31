## Benign or Malignant Tumor App

The web app was created using Flask and is currently only available on the local drive.

### Explanation of Files

1. `main.py` - This is the main Python code that uses Flask and calls make_prediction.py to use the model
2. `make_prediction.py` - This is a separate Python script that reads in the pickled model and also preps the data for the model
3. `logit_pickled.p` - The pickled model
4. `scaler.p` - The pickled scaler 
5. `templates/index.html` - This is the webpage that will be able to take inputs for the model and output a result on the webpage
