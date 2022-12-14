
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd

# def knn(train_data, train_labels, test_data, test_labels, k):
#     """
#     Performs k-NN on the given data.
#     """

#     neighbours = KNeighborsClassifier(n_neighbors=k)
#     neighbours.fit(train_data, train_labels)
#     pred_labels = neighbours.predict(test_data)

#     acc = accuracy_score(test_labels, pred_labels)
#     f1 = f1_score(test_labels, pred_labels, average="weighted")

#     return acc, f1, pred_labels


# def knn_cross_validation(data, labels, k):
#     """
#     Evaluates k-NN using 10-fold cross validation on the given data.
#     """

#     # Cross validation settings
#     kf = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)

#     # Create the k-NN classifier
#     clf = KNeighborsClassifier(n_neighbors=k)

#     result = cross_validate(clf, data, labels, cv=kf, scoring=[
#                             "accuracy", "f1_weighted"])
#     test_acc = result["test_accuracy"].mean()
#     test_f1 = result["test_f1_weighted"].mean()

#     return test_acc, test_f1


def knn_gridsearch(data, labels, parameters, scoring):
    """
    knn_gridsearch()
     - Performs gridsearch for kNN on the given data.
    """

    # Extract parameters
    k_range = parameters["k_range"]

    # Create dataframe for storage
    knn_results = pd.DataFrame(
        [], columns=["param_n_neighbors", "mean_train_score", "mean_test_score"])

    # Define the model
    knn_model = KNeighborsClassifier()
    parameters = {'n_neighbors': [i for i in k_range]}

    clf = GridSearchCV(knn_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)
    clf.fit(data, labels)

    # knn_results = pd.DataFrame(clf.cv_results_)

    # knn_results = pd.concat([knn_results, df])
    # knn_results = knn_results.sort_values(
    #     by=['mean_test_score'], ascending=False)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
