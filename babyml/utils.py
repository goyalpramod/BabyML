"""
Helper functions for BabyML.
"""

import random

# TODO: Add documentation 

def train_test_split(
        X : list = [],
        y : list = [],
        train_size : float = 0.8,
        test_size : float = 0.2,
        random_seed : int = 42,
        shuffle : bool = False):
    
    if not shuffle:
        
        X_train = X[:int(len(X)*train_size)]
        X_test = X[int(len(X)*test_size):]
        y_train = y[:int(len(y)*train_size)]
        y_test = y[int(len(y)*test_size):]
        
        return X_train, X_test, y_train, y_test
    else:
        random.seed(random_seed)
        combined = list(zip(X, y))
        random.shuffle(combined)
        X[:], y[:] = zip(*combined)
        X_train = X[:int(len(X)*train_size)]
        X_test = X[int(len(X)*test_size):]
        y_train = y[:int(len(y)*train_size)]
        y_test = y[int(len(y)*test_size):]
        return X_train, X_test, y_train, y_test
    
def log_loss():
    pass

def accuracy_score():
    pass

def confusion_matrix():
    pass