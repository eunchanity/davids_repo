from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator


def elbow_kplot(matrix):
    """
    input: matrix of word2vec dimensions
    output: plot of elbow method
    """

    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 24,
    }

    # a list holds the SSE values for each k
    sse = []
    for k in range(1, 11):
        kmeans_elbow = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans_elbow.fit(matrix)
        sse.append(kmeans_elbow.inertia_)

    # plot elbow method
    plt.style.use("fivethirtyeight")
    plt.plot(range(1, 11), sse)
    plt.xticks(range(1, 11))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()

    return


def elbow_kvalue(matrix):
    """
    input: matrix of word2vec dimensions
    output: elbow k value
    """

    kmeans_kwargs = {
        "init": "random",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 24,
    }

    # a list holds the SSE values for each k
    sse = []
    for k in range(1, 11):
        kmeans_elbow = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans_elbow.fit(matrix)
        sse.append(kmeans_elbow.inertia_)

    # elbow k value
    kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")

    return kl.elbow
