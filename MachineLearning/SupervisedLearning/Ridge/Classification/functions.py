from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import RidgeClassifier


def ridge_gridsearch(X, y, parameters, scoring):
    """
    ridge_gridsearch()
     - Performs gridsearch for Ridge on the given data.
    """

    # Extract hyperparameters
    parameters = {
        "alpha": parameters["alpha"],
    }

    # Define the model
    _model = RidgeClassifier()

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
