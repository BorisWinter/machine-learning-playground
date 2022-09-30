from sklearn.model_selection import GridSearchCV
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


def QDA_gridsearch(X, y, parameters, scoring):
    """
    QDA_gridsearch()
     - Performs gridsearch for QDA on the given data.
    """

    # Extract hyperparameters
    parameters = {
        "reg_param": parameters["reg_param"],
    }

    # Define the model
    _model = QuadraticDiscriminantAnalysis()

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
