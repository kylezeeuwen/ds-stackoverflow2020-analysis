from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from helpers import clone_drop_and_convert, clone_impute_data, perf_measures, round_decision, reduce_dataframe_using_min_non_null

def apply_linear_regression_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = LinearRegression(normalize=True)
    model.fit(X_train, y_train)

    y_train_preds = round_decision(model.predict(X_train))
    y_test_preds = round_decision(model.predict(X_test))
       
    feature_count = X.shape[1]
    dataset_count = X.shape[0]

    metrics = perf_measures(y_test.array, y_test_preds)
      
    return metrics, model