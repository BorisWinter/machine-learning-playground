from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC


def SVM_gridsearch(X, y, parameters, scoring):
    """
    SVM_gridsearch()
     - Performs gridsearch for SVC on the given data.
    """

    # Extract hyperparameters
    parameters = {
        "kernel": parameters["kernels"],
        'C': parameters["C_range"]
    }

    # Define the model
    _model = SVC()

    # Perform gridsearch
    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)

    # Fit the best model
    clf.fit(X, y)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
