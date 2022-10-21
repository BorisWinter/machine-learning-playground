from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB


def naive_bayes_gridsearch(X, y, parameters, scoring):
    """
    naive_bayes_gridsearch()
     - Performs gridsearch for naive bayes on the given data.
    """

    # Extract hyperparameters
    # TODO: Add penalty-solver combinations.
    parameters = {
        'var_smoothing': parameters["var_smoothing"]
    }

    # Define the model
    _model = GaussianNB()

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
