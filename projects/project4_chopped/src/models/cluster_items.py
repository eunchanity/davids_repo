def cluster_6(item_labels, fit_kmeans):
    """
    input: item_labels (list) list of labels for corresponding data matrix, fit_kmeans(variable) data matrix fit to KMeans
    output: items within each cluster
    """

    cluster_dict = dict(zip(item_labels, fit_kmeans.labels_))

    # cluster list size can expand as needed
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    cluster_4 = []
    cluster_5 = []
    cluster_6 = []

    for k, v in cluster_dict.items():
        if v == 0:
            cluster_1.append(k)
        elif v == 1:
            cluster_2.append(k)
        elif v == 2:
            cluster_3.append(k)
        elif v == 3:
            cluster_4.append(k)
        elif v == 4:
            cluster_5.append(k)
        elif v == 5:
            cluster_6.append(k)
    return cluster_1, cluster_2, cluster_3, cluster_4, cluster_5, cluster_6


def cluster_4(item_labels, fit_kmeans):
    """
    input: item_labels (list) list of labels for corresponding data matrix, fit_kmeans(variable) data matrix fit to KMeans
    output: items within each cluster
    """

    cluster_dict = dict(zip(item_labels, fit_kmeans.labels_))

    # cluster list size can expand as needed
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    cluster_4 = []

    for k, v in cluster_dict.items():
        if v == 0:
            cluster_1.append(k)
        elif v == 1:
            cluster_2.append(k)
        elif v == 2:
            cluster_3.append(k)
        elif v == 3:
            cluster_4.append(k)

    return cluster_1, cluster_2, cluster_3, cluster_4


def cluster_5(item_labels, fit_kmeans):
    """
    input: item_labels (list) list of labels for corresponding data matrix, fit_kmeans(variable) data matrix fit to KMeans
    output: items within each cluster
    """

    cluster_dict = dict(zip(item_labels, fit_kmeans.labels_))

    # cluster list size can expand as needed
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    cluster_4 = []
    cluster_5 = []

    for k, v in cluster_dict.items():
        if v == 0:
            cluster_1.append(k)
        elif v == 1:
            cluster_2.append(k)
        elif v == 2:
            cluster_3.append(k)
        elif v == 3:
            cluster_4.append(k)
        elif v == 4:
            cluster_5.append(k)

    return cluster_1, cluster_2, cluster_3, cluster_4, cluster_5
