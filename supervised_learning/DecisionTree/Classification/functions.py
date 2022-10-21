from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier


def decision_tree_gridsearch(X, y, parameters, scoring):
    """
    decision_tree_gridsearch()
     - Performs gridsearch for SVC on the given data.
    """

    # Extract hyperparameters
    parameters = {
        "criterion": parameters["criterion"],
        # 'max_depth': parameters["max_depth"]
    }

    # Define the model
    _model = DecisionTreeClassifier(random_state=42)

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
