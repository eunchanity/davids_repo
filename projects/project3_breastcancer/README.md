# Classifying Benign/Malignant Tumors for Breast Cancer

## Project 3 at Metis

**Objective**: Build a classification model to predict whether a breast cancer cell will be benign or malignant based on cell characteristics.

**Overview**:

- Acquire dataset and create a database in postgresql on an AWS machine
- Access database using SQLalchemy
- Select a classification model through cross-validation: - k-nearest neighbors, logistic regression, decision tree, random forest, gaussian naive bayes, support vector machine
- Tune selected model through hyperparameters, threshold, class imbalance, feature selection
- Interpret data: confusion matrix, precision, model coefficients
- Visualize data: Tableau, Flask

### Setup

#### 1) Access project3_breastcancer.ipynb in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project3_breastcancer/notebooks" target="_blank">notebooks folder</a> to follow data analysis and modeling

- Database import using SQLalchemy
- Model selection through cross-validation
- Model tuning through class weight adjustment, hyperparameter optimization, feature selection
- Interpretation of results

#### 2) Access the models in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project3_breastcancer/src/models" target="_blank">src/models folder</a> to follow the modeling process and code

- Cross-validation on train set
- Cross-validation on train set with adjusted class weights
- Logistic regression on test set

#### 3) Access the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project3_breastcancer/apps/flask" target="_blank">apps/flask folder</a> to test out a local Flask web app

- Import the fit logistic regression model, which was saved through pickling
- Deployment of the model on Flask
- Predict benign/malignant tumor using user-inputs of tumor characteristics
- The app has also been made available at <a href="https://breast-cancer-tumor-classifer.herokuapp.com/" target="_blank">https://breast-tumor-classifier.herokuapp.com</a>

#### 4) Access project3_breastcancer.pdf in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project3_breastcancer/reports" target="_blank">reports folder</a> to follow the presentation deck

- Presentation of model creation and model outputs
- Implications of the model's results
- Additional considerations
- The presentation can also be followed in my blog: <a href="https://eunchanity.github.io/breast-cancer/" target="_blank">Classifying Breast Cancer Tumors with Machine Learning</a><br/>

---
