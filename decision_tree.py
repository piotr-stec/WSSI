import numpy as np
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.root = self._grow_tree(X, y)

    # Buduje rekurencyjnie drzewo jeżeli głębokość jest > max_depth ilość klas(label) w y == 1 albo liczba przykładowych danych
    # shape[0] jest mniejsza od min_samples_split to zwraca Node z wartością value jako najczęściej występująca cecha w y
    # Counter(y).most_common(1)[0][0]
    # W innym przypadku losowo wybiera cechy w ilosci self n_features z ilości cech w danych czyli shape[1]
    # wybiera najlepszą ceche
    def _grow_tree(self, X, y, depth=0):
        n_samples = X.shape[0]
        n_feat = X.shape[1]
        n_labels = np.unique(y)
        feat_idxs = np.random.choice(n_feat, self.n_features, replace=False)



    # szuka najlepszego ig dla wszystkich możliwych feat_idxs i ich thresholdow i zwraca najlepszy index cechy i threshold
    def _best_split(self, X, y, feat_idxs):
        best_threshold = None
        best_feature = None
        best_ig = 0
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                ig = self._information_gain(y, X_column, threshold)
                if ig > best_ig:
                    best_ig = ig
                    best_feature = feat_idx
                    best_threshold = threshold
        return best_threshold, best_feature




    # oblicza ig dla kolumny dziele wzgl threshold na lewy i prawy i dla nich entropia zwracam parent entropy - ważona dzieci
    def _information_gain(self, y, X_column, threshold):
        parent_entropy = self._entropy(y)
        left_indexes, right_indexes = self._split(X_column, threshold)
        n_left = len(left_indexes)
        n_right = len(right_indexes)
        n = len(y)
        left_child_entropy = self._entropy(y[left_indexes])
        right_child_entropy = self._entropy(y[right_indexes])
        weighted_average_child = (n_left/n) * left_child_entropy + (n_right/n) * right_child_entropy
        return parent_entropy - weighted_average_child

    def _split(self, X_column, split_threshold):
        left_idxs = np.where(X_column <= split_threshold)[0]
        right_idxs = np.where(X_column > split_threshold)[0]
        return left_idxs, right_idxs

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return - np.sum([p * np.log(p) for p in ps if p > 0])

    def _traverse_tree(self, x, node):
        pass

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])



