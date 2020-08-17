from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.metrics import silhouette_score


def silhouette_plot(matrix):
    """
    input: matrix of word2vec dimensions
    output: plot of silhouette method
    """

    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 24,
    }

    # a list holds the silhouette coefficients for each k
    silhouette_coefficients = []

    # start at 2 clusters for silhouette coefficient
    for k in range(2, 11):
        kmeans_silhouette = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans_silhouette.fit(matrix)
        score = silhouette_score(matrix, kmeans_silhouette.labels_)
        silhouette_coefficients.append(score)

    plt.style.use("fivethirtyeight")
    plt.plot(range(2, 11), silhouette_coefficients)
    plt.xticks(range(2, 11))
    plt.xlabel("Number of Clusters")
    plt.ylabel("Silhouette Coefficient")
    plt.show()
