from typing import Optional

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
    """
    Find the mathematical formulation used by sklearn here: https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation
    This part from a course by CMU was extremely helpful: https://www.cs.cmu.edu/~bhiksha/courses/10-601/decisiontrees/
    And this blog too: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
    """
    def __init__(
        self,
        criterion : str ="gini",
        max_depth : Optional[int] = None,
        min_samples_split : int = 2,
        max_features : Optional[int] = None,
        random_seed : int = 42,):
        """        
        Parameters
        ----------
        criterion : {'gini', 'entropy'}, default='gini'
            The function to measure split quality.
        """
        self.criterion = criterion
    
    def fit(self, X, y):
        len_attributes = len(X[0])
        len_instance = len(X)


    def calculate_gini_index(self, y):
        """
        The mathematical formula for gini index is given by 

        """
        gini_impurity = 1
        unique_labels = set(y)
        n = len(y)
        for label in unique_labels:
            count = y.count(label)  
            probability = count / n
            gini_impurity -= probability ** 2
        return gini_impurity

    def calculate_entropy(self,y):
        from math import log

        entropy = 0
        unique_labels = set(y)
        n = len(y)
        for label in unique_labels:
            count = y.count(label)
            prob = count/n
            entropy -= prob*log(prob)
        return entropy

    def calculate_information_gain(self):
        pass



class KNNClassifier:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
        self.data = None
        self.labels = None

