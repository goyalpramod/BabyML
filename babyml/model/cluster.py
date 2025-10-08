class KMeansCluster:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.centroids = None