import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

def apply_linear_regression_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = LinearRegression(normalize=True)
    model.fit(X_train, y_train)

    y_train_preds = round_decision(model.predict(X_train))
    y_test_preds = round_decision(model.predict(X_test))
       
    metrics = compute_performance_metrics(y_test.array, y_test_preds)
      
    return metrics, model, 'linear_regression'

def apply_svm_model (X, y, kernel='linear'):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = svm.SVC(kernel)
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = compute_performance_metrics(y_test.array, y_test_preds)
      
    return metrics, model, 'svm_%s' % kernel

def apply_linear_svm_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = svm.LinearSVC()
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = compute_performance_metrics(y_test.array, y_test_preds)
      
    return metrics, model, 'linear_svm'

def apply_random_forest_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42) 

    model = RandomForestClassifier(min_samples_leaf=20)
    model.fit(X_train, y_train)

    y_train_preds = model.predict(X_train)
    y_test_preds = model.predict(X_test)
    
    metrics = compute_performance_metrics(y_test.array, y_test_preds)
      
    return metrics, model, 'random_forest'

def divide_or_zero (a, b):
    return a / b if b != 0 else 0

def compute_performance_metrics(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    P = 0
    N = 0

    for i in range(len(y_hat)):
        if y_actual[i]==1:
           P += 1
        if y_actual[i]==0:
           N += 1
        if y_actual[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FP += 1
        if y_actual[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
           FN += 1

    # source: https://en.wikipedia.org/wiki/Sensitivity_and_specificity
    #sensitivity, recall, hit rate, or true positive rate (TPR)
    TPR = divide_or_zero(TP, P)

    #specificity, selectivity or true negative rate (TNR)
    TNR = divide_or_zero(TN, N)

    #precision or positive predictive value (PPV)
    PPV = divide_or_zero(TP, (TP + FP))

    #precision or positive predictive value (PPV)
    NPV = divide_or_zero(TN, (TN + FN))

    # accuracy
    ACC = divide_or_zero((TP + TN), (P + N))

    return {
        "P": P,
        "N": N,
        "TP": TP,
        "FP": FP,
        "TN": TN,
        "FN": FN,
        "TPR": TPR,
        "TNR": TNR,
        "PPV": PPV,
        "NPV": NPV,
        "ACC": ACC,
    }

def round_decision (arr):
    rounder = lambda x: 1 if x >= 0.5 else 0
    return np.array([rounder(xi) for xi in arr])
