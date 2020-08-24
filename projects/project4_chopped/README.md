# Creating a Chopped Mystery Basket Generator and Ingredient Recommender

## Project 4 at Metis

**Objective**: Use natural langauge processing (NLP) and unsupervised learning to create a recommendation system that generates a random "Chopped" basket.

**Overview**:

- Acquire dataset and preprocess the text data using NLP
- Create word vectors and reduce dimensionality using word2vec
- Select an unsupervised learning model (clustering) to group the text data: k-means clustering, hierarchical clustering
- Determine the label for each cluster based on the elements within the cluster
- Create a "Chopped Basket Generator" app using Streamlit that recommends a basket of 4 random ingredients based on user selection.

### Setup

#### 1) Access project4_chopped.ipynb in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project4_chopped/notebooks" target="_blank">notebooks folder</a> to follow data analysis and modeling

- Proprocessing text using NLTK
- Word vectorization using word2vec
- Model selection for unsupervised learning: k-means clustering, hierarchical clustering
- Recommendation system for randomly generated basket

#### 2) Access the models in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project4_chopped/src/models" target="_blank">src/models folder</a> to follow the modeling process and code

- K-means clustering optimal k selection using elbow method
- K-means clustering optimal k selection using silhouette score
- Separating out the individual items to their respective clusters

#### 3) Access the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project4_chopped/src/models" target="_blank">streamlit folder</a> to test out a local Streamlit web app

- Import the clusters, pickled from the notebook
- Deployment of the "Chopped Basket Generator" on Streamlit
- The app has also been made available at <a href="https://chopped-basket-generator.herokuapp.com/" target="_blank">https://chopped-basket-generator.herokuapp.com/</a>

#### 4) Access project4_chopped.pdf in the <a href="https://github.com/eunchanity/davids_repo/tree/master/projects/project4_chopped/reports" target="_blank">reports folder</a> to follow the presentation deck

- Presentation of model creation and model outputs
- Implications of the model's results
- Additional considerations
- The presentation can also be followed in my blog: <a href="https://eunchanity.github.io/chopped/" target="_blank">Creating a Mystery Basket Generator from the TV Show "Chopped"</a><br/>

---
