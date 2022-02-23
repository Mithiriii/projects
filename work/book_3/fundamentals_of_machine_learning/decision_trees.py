from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz, DecisionTreeRegressor

iris = load_iris()
X = iris.data[:, 2:]    # długość i szerokość płatka
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)

export_graphviz(
    tree_clf,
    out_file="iris_drzewo.dot",
    feature_names=iris.feature_names[2:],
    class_names=iris.target_names,
    rounded=True,
    filled=True
)


# drzewo regresyjne
tree_reg = DecisionTreeRegressor(max_depth=2)
tree_reg.fit(X, y)