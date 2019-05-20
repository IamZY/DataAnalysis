from sklearn.datasets import load_iris
from sklearn import tree
import pandas as pd
import pydotplus

iris = load_iris()

# print(iris.data)
# print(iris.target)

iris_pd = pd.DataFrame(iris.data,columns=['SpealLength', 'Spealwidth', 'PetalLength', 'PetalLength'])

print(iris_pd)

print(iris.target)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")