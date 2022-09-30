from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression


def logistic_regression_gridsearch(X, y, parameters, scoring):
    """
    logistic_regression_gridsearch()
     - Performs gridsearch for logistic regression on the given data.
    """

    # Extract hyperparameters
    # TODO: Add penalty-solver combinations.
    parameters = {
        'C': parameters["C_range"]
    }

    # Define the model
    _model = LogisticRegression()

    clf = GridSearchCV(_model, parameters, cv=10,
                       return_train_score=True, scoring=scoring, verbose=0)
    clf.fit(X, y)

    # knn_results = pd.DataFrame(clf.cv_results_)

    # knn_results = pd.concat([knn_results, df])
    # knn_results = knn_results.sort_values(
    #     by=['mean_test_score'], ascending=False)

    return clf.cv_results_, clf.best_estimator_, clf.best_score_
