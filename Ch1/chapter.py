#%%
from sklearn.datasets import load_iris

dataset = load_iris()
X = dataset.data
Y = dataset.target
print(dataset.DESCR)

attribute_means = X.mean(axis=0)
# X_d = np.arr

from collections import defaultdict
from operator import itemgetter

def train_feature_value(X, y_true, feature_index, value):
    class_counts = defaultdict(int)
    for sample, y in zip(X, y_true):
        if sample[feature_index] == value:
            class_counts[y] += 1
    
    sorted_class_counts = sorted(class_counts.item(), key=itemgetter(1), reverse=True)
    most_frequent_class = sorted_class_counts[0][0]
    incorrect_predictions = [class_count for class_value, class_count in class_counts.item() if class_value != most_frequent_class]
    error = sum(incorrect_predictions)
    return most_frequent_class, error

