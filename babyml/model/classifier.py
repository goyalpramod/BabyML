class LogisticRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None

class SVMClassifier:
    def __init__(self, kernel='linear'):
        self.kernel = kernel
        self.support_vectors = None
        self.coefficients = None
        self.intercept = None

class RandomForestClassifier:
    def __init__(self, n_trees=100):
        self.n_trees = n_trees
        self.trees = []

class NaiveBayesClassifier:
    def __init__(self):
        self.class_priors = None
        self.likelihoods = None


class DecisionTreeClassifier:
    def __init__(self):
        self.tree = None

class KNNClassifier:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
        self.data = None
        self.labels = None

