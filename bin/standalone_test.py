import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, confusion_matrix

import disarray
# %matplotlib inline

pd.options.display.max_rows = 2000
pd.options.display.max_columns = 1000
pd.options.display.max_colwidth = 255

df = pd.read_csv('./assets/survey_results_public.csv')
schema = pd.read_csv('./assets/survey_results_schema.csv')

DUMMY_NA = True
FILL="Mode"

# use respondent as the index
if 'Respondent' in df.columns:
    df.set_index('Respondent')

# Exclude CompTotal as it is pre converted and normalised to annual USD , which is stored in ConvertedComp
if 'CompTotal' in df.columns:
    df.drop(columns=['CompTotal'], inplace=True)

# convert these near numerics to a numeric Series
from helpers import convert_age_series_to_numeric
df['YearsCode'] = df['YearsCode'].map(convert_age_series_to_numeric)
df['YearsCodePro'] = df['YearsCodePro'].map(convert_age_series_to_numeric)
df['Age1stCode'] = df['Age1stCode'].map(convert_age_series_to_numeric)

country_subset = df.query("Country in ['United States', 'Canada', 'United Kingdom', 'Australia', 'New Zealand']")[[
    'Country',
    'Age',
    'Age1stCode',
    'ConvertedComp',
    'Employment',
    'JobSat',
    'JobSeek',
    'MainBranch',
    'NEWEdImpt',
    'OpSys',
    'OrgSize',
    'UndergradMajor',
    'WorkWeekHrs',
    'YearsCode',
    'YearsCodePro'
]]

def perf_measures(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FP += 1
        if y_actual[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
           FN += 1

    return (TP, FP, TN, FN)

def count_ones_ratio (arr):
    s = pd.Series(arr)
    return s[s == 1].shape[0] / arr.size

def round_decision (arr):
    rounder = lambda x: 1 if x >= 0.5 else 0
    return np.array([rounder(xi) for xi in arr])

def clean_data (df, dummy_na, fill_technique):
    categorical_only_columns = df.select_dtypes(include='object').columns
    for column in categorical_only_columns:
        if column == 'Country':
            continue
        # for each cat add dummy var, drop original column
        df = pd.concat([df.drop(column, axis=1), pd.get_dummies(df[column], prefix=column, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)

    fill_mean = lambda col: col.fillna(col.mean())
    fill_mode = lambda col: col.fillna(col.mode()[0])
    fill = fill_mean if FILL == "Mean" else fill_mode
    df['YearsCodePro'] = fill(df['YearsCodePro'])
    df['Age'] = fill(df['Age'])
    df['Age1stCode'] = fill(df['Age1stCode'])
    df['ConvertedComp'] = fill(df['ConvertedComp'])
    df['WorkWeekHrs'] = fill(df['WorkWeekHrs'])
    df['YearsCode'] = fill(df['YearsCode'])
    df['YearsCodePro'] = fill(df['YearsCodePro'])

    is_usa = lambda country: 1 if country == 'United States' else 0
    df['is_usa'] = df['Country'].map(is_usa)

    # predict is_usa using linear classifier
    X_columns = [ elem for elem in df.columns if elem not in ['Country', 'is_usa' ]]
    y_column = 'is_usa'
    X = df[X_columns]
    y = df[y_column]

    return X, y

def apply_linear_regression_model (X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .30, random_state=42)

    model = LinearRegression(normalize=True)
    model.fit(X_train, y_train)

    y_train_preds = round_decision(model.predict(X_train))
    y_test_preds = round_decision(model.predict(X_test))

    r2_train_score = r2_score(y_train, y_train_preds)
    r2_test_score = r2_score(y_test, y_test_preds)

    ones_train_ratio = count_ones_ratio(y_train_preds)
    ones_test_ratio = count_ones_ratio(y_test_preds)

    feature_count = X.shape[1]
    dataset_count = X.shape[0]

    # https://stackoverflow.com/questions/31324218/scikit-learn-how-to-obtain-true-positive-true-negative-false-positive-and-fal
    # https://github.com/arvkevi/disarray

    TP, FP, TN, FN = perf_measures(y_test.array, y_test_preds)

# #     cm = confusion_matrix(y_test, y_test_preds)
# #     metrics = pd.DataFrame(cm, dtype=int)
# #     print(metrics.da)
# #     print(metrics.da.precision)
    print("TP", TP)
    print("TN", TN)
    print("FP", FP)
    print("FN", FN)

#     return feature_count, dataset_count, r2_train_score, r2_test_score, ones_train_ratio, ones_test_ratio
    return cm

X, y = clean_data(country_subset, dummy_na=True, fill_technique="Mean")
# feature_count, dataset_count, r2_train_score, r2_test_score, ones_train_ratio, ones_test_ratio = apply_linear_regression_model(X, y)
cm = apply_linear_regression_model(X, y)