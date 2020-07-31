from flask import Flask, request, render_template
from make_prediction import benign_malignant
import numpy as np

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route("/")
def entry_page():
    return render_template("index.html")


# creates an association between the /predict_tumor page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route("/predict_tumor/", methods=["GET", "POST"])
def render_message():

    # user-entered characteristics
    characteristics = [
        "clumpthickness",
        "uniformcellsize",
        "margadhesion",
        "epithelial",
        "barenuclei",
        "blandchromatin",
        "normalnucleoli",
        "mitoses",
    ]

    # error messages to ensure correct range
    messages = [
        "The clump thickness value must be a number from 1-10.",
        "The uniformity of cell size value must be a number from 1-10.",
        "The marginal adhesion value must be a number from 1-10.",
        "The single epithelial cell size value must be a number from 1-10.",
        "The bare nuclei value must be a number from 1-10.",
        "The bland chromatin value must be a number from 1-10.",
        "The normal nucleoli value must be a number from 1-10.",
        "The mitoses value must be a number from 1-10.",
    ]

    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(characteristics):
        user_input = request.form[ing]
        try:
            float_characteristics = float(user_input)
            if float_characteristics < 1 or float_characteristics > 10:
                raise ValueError()
        except:
            return render_template("index.html", message=messages[i])
        amounts.append(float_characteristics)

    # show user final message
    final_message = benign_malignant(np.array(amounts).reshape(1, -1))
    return render_template("index.html", message=final_message)


if __name__ == "__main__":
    app.run(debug=True)
