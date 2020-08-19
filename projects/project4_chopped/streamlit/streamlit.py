import streamlit as st
import pandas as pd
import numpy as np
import pickle
import random

# read in pickled cluster lists
app_sauce_garnish = pickle.load(open("pickle/app1.p", "rb"))
app_processed_sweet = pickle.load(open("pickle/app2.p", "rb"))
app_seafood = pickle.load(open("pickle/app3.p", "rb"))
app_protein_carbs = pickle.load(open("pickle/app4.p", "rb"))
app_vegetables = pickle.load(open("pickle/app5.p", "rb"))
app_fruits = pickle.load(open("pickle/app6.p", "rb"))
ent_fruits_vegetables = pickle.load(open("pickle/ent1.p", "rb"))
ent_seafood = pickle.load(open("pickle/ent2.p", "rb"))
ent_random = pickle.load(open("pickle/ent3.p", "rb"))
ent_protein_carbs = pickle.load(open("pickle/ent4.p", "rb"))
des_fruits = pickle.load(open("pickle/des1.p", "rb"))
des_liquids = pickle.load(open("pickle/des2.p", "rb"))
des_dairy_sauces = pickle.load(open("pickle/des3.p", "rb"))
des_random = pickle.load(open("pickle/des4.p", "rb"))
des_sugar_snacks = pickle.load(open("pickle/des5.p", "rb"))

# streamlit outline
st.title('"Chopped" Basket Generator')

meals = {"Appetizer": "Appetizer", "Entree": "Entree", "Dessert": "Dessert"}
choice = st.selectbox(
    "Which basket type would you like to create?", list(meals.keys()), 0
)

# appetizer selection
if meals[choice] == "Appetizer":
    st.subheader("Appetizer Round")
    st.write("What would you like to include for your appetizer basket?")
    app1 = st.checkbox("Protein/Carbs")
    app2 = st.checkbox("Seafood")
    app3 = st.checkbox("Vegetables")
    app4 = st.checkbox("Fruits")
    app5 = st.checkbox("Processed/Sweets")
    app6 = st.checkbox("Sauces/Garnish")

    if st.button("Generate a Random Basket!"):

        def appetizer(app1, app2, app3, app4, app5, app6):
            """
            input: user selections for appetizer checkbox
            output: 4 random ingredients from selected clusters
            """
            select = []
            if app1 == True:
                select += app_protein_carbs
            elif app2 == True:
                select += app_seafood
            elif app3 == True:
                select += app_vegetables
            elif app4 == True:
                select += app_fruits
            elif app5 == True:
                select += app_processed_sweet
            elif app6 == True:
                select += app_sauce_garnish

            return select

        choices = appetizer(app1, app2, app3, app4, app5, app6)
        results = random.sample(choices, 4)
        st.write(results)

    else:
        st.write("")

# entree selection
elif meals[choice] == "Entree":
    st.subheader("Entree Round")
    st.write("What would you like to include for your entree basket?")
    ent1 = st.checkbox("Protein/Carbs")
    ent2 = st.checkbox("Seafood")
    ent3 = st.checkbox("Fruits/Vegetables")
    ent4 = st.checkbox("Mystery Ingredient")

    if st.button("Generate a Random Basket!"):

        def entree(ent1, ent2, ent3, ent4):
            """
            input: user selections for entree checkbox
            output: 4 random ingredients from selected clusters
            """
            select = []
            if ent1 == True:
                select += ent_protein_carbs
            elif ent2 == True:
                select += ent_seafood
            elif ent3 == True:
                select += ent_fruits_vegetables
            elif ent4 == True:
                select += ent_random

            return select

        choices = entree(ent1, ent2, ent3, ent4)
        results = random.sample(choices, 4)
        st.write(results)
    else:
        st.write("")

# dessert selection
elif meals[choice] == "Dessert":
    st.subheader("Dessert Round")
    st.write("What would you like to include for your dessert basket?")
    des1 = st.checkbox("Sugar/Snacks")
    des2 = st.checkbox("Fruits/Vegetables")
    des3 = st.checkbox("Liquids")
    des4 = st.checkbox("Dairy/Sauces")
    des5 = st.checkbox("Mystery Ingredient")

    if st.button("Generate a Random Basket!"):

        def dessert(des1, des2, des3, des4, des5):
            """
            input: user selections for dessert checkbox
            output: 4 random ingredients from selected clusters
            """
            select = []
            if des1 == True:
                select += des_sugar_snacks
            elif des2 == True:
                select += des_fruits
            elif des3 == True:
                select += des_liquids
            elif des4 == True:
                select += des_dairy_sauces
            elif des5 == True:
                select += des_random

            return select

        choices = dessert(des1, des2, des3, des4, des5)
        results = random.sample(choices, 4)
        st.write(results)
    else:
        st.write("")
