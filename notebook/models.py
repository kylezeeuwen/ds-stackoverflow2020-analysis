from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from helpers import clone_drop_and_convert, clone_impute_data, perf_measures, round_decision, reduce_dataframe_using_min_non_null

def apply_linear_regression_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = LinearRegression(normalize=True)
    model.fit(X_train, y_train)

    y_train_preds = round_decision(model.predict(X_train))
    y_test_preds = round_decision(model.predict(X_test))
       
    metrics = perf_measures(y_test.array, y_test_preds)
      
    return metrics, model, 'linear_regression'

def apply_svm_model (X, y, kernel='linear'):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = svm.SVC(kernel)
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = perf_measures(y_test.array, y_test_preds)
      
    return metrics, model, 'svm_%s' % kernel

def apply_linear_svm_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = svm.LinearSVC()
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = perf_measures(y_test.array, y_test_preds)
      
    return metrics, model, 'linear_svm'

def apply_random_forest_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = RandomForestClassifier(min_samples_leaf=20)
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = perf_measures(y_test.array, y_test_preds)
      
    return metrics, model, 'random_forest'
