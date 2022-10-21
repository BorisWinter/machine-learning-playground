from sklearn.model_selection import GridSearchCV
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def LDA_gridsearch(X, y, parameters, scoring):
    """
    LDA_gridsearch()
     - Performs gridsearch for LDA on the given data.
    """

    # Extract hyperparameters
    parameters = {
        "solver": parameters["solver"],
    }

    # Define the model
    _model = LinearDiscriminantAnalysis()

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
