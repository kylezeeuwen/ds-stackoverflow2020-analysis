import pandas as pd
import numpy as np

from convert_multiple_choice_to_dataframe import convert_multiple_choice_to_dataframe

def reduce_dataframe_using_min_non_null (input_df, min_non_null_cutoff):
    df = input_df.copy()
    categorical_dummies = df.select_dtypes(include='uint8') # imprecise as uint8 does not imply a dummied categorical column
    columns_to_drop = categorical_dummies[categorical_dummies.columns[categorical_dummies.sum()<min_non_null_cutoff]].columns
    return df.drop(columns=columns_to_drop)

def clone_drop_and_convert (input_df):
    df = input_df.copy()
    
    # use respondent as the index
    if 'Respondent' in df.columns:    
        df.set_index('Respondent')

    # Exclude CompTotal and CompFreq as they are free form and not in a standard currency, use ConvertedComp which is normalised to annual USD
    # these would also serve as "unfair" predictors of country so they will skew our results if left in the dataset
    for raw_compensation_column in ['CompTotal', 'CompFreq', 'CurrencyDesc', 'CurrencySymbol']:
        if raw_compensation_column in df.columns:
            df.drop(columns=[raw_compensation_column], inplace=True)

    # these columns are strings but they contain mostly numbers, with a few inequality strings to represent the boundaries,
    # convert them to numeric so we can treat as a quant metric:
    #   * 'More than 50 years' -> 51
    #   * 'Younger than 5 years' -> 4
    #   * 'Older than 85' -> 86
    #   * 'Less than 1 year' -> 0
    df['YearsCode'] = df['YearsCode'].map(_convert_age_series_to_numeric)
    df['YearsCodePro'] = df['YearsCodePro'].map(_convert_age_series_to_numeric)
    df['Age1stCode'] = df['Age1stCode'].map(_convert_age_series_to_numeric)
        
    return df

def clone_and_convert_multiple_choice_columns (input_df):
    df = input_df.copy()
    
    multiple_choice_columns = [
        'DatabaseDesireNextYear',
        'DatabaseWorkedWith',
        'DevType',
        'EdLevel',
        'Employment',
        'Ethnicity',
        'Gender',
        'JobFactors',
        'JobSeek',
        'LanguageDesireNextYear',
        'LanguageWorkedWith',
        'MiscTechDesireNextYear',
        'MiscTechWorkedWith',
        'NEWCollabToolsDesireNextYear',
        'NEWCollabToolsWorkedWith',
        'NEWJobHunt',
        'NEWJobHuntResearch',
        'NEWPurchaseResearch',
        'NEWSOSites',
        'NEWStuck',
        'PlatformDesireNextYear',
        'PlatformWorkedWith',
        'Sexuality',
        'WebframeDesireNextYear',
        'WebframeWorkedWith',
    ]
    
    for column in multiple_choice_columns:
        dummied_df = convert_multiple_choice_to_dataframe(df[column])
        df = df.merge(dummied_df, how='inner', left_index=True, right_index=True, validate='1:1')
        
    df.drop(columns=multiple_choice_columns, inplace=True)    
    
    return df
    
def _convert_age_series_to_numeric (input_string):
    if input_string == 'Less than 1 year':
        return 0
    if input_string == 'More than 50 years':
        return 51
    if input_string == 'Younger than 5 years':
        return 4
    if input_string == 'Older than 85':
        return 86

    # cheap NaN check
    if input_string != input_string:
        return input_string
    
    return int(input_string)

def divide_or_zero (a, b):
    return a / b if b != 0 else 0

def perf_measures(y_actual, y_hat):
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

def clone_impute_data (input_df, dummy_na, fill_technique):
    df = input_df.copy()
    for column in df.select_dtypes(include='object').columns:
        if column == 'Country':
            continue
        # for each cat add dummy var, drop original column
        df = pd.concat([df.drop(column, axis=1), pd.get_dummies(df[column], prefix=column, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)    

    fill_mean = lambda col: col.fillna(col.mean())
    fill_mode = lambda col: col.fillna(col.mode()[0])
    fill = fill_mean if fill_technique == "Mean" else fill_mode

    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        df[column] = fill(df[column])

    return df    

def get_coefficent_weights(coefficients, columns):
    '''
    INPUT:
    coefficients - the coefficients of the linear model 
    columns - the column in the x training set
    OUTPUT:
    coefs_df - a dataframe holding the coefficient, estimate, and abs(estimate)
    
    Provides a dataframe that can be used to understand the most influential coefficients
    in a linear model by providing the coefficient estimates along with the name of the 
    variable attached to the coefficient.
    '''
    coefs_df = pd.DataFrame()
    coefs_df['X_Column'] = columns
    coefs_df['weight'] = coefficients
    coefs_df['abs_weight'] = np.abs(coefficients)
    return coefs_df.sort_values('abs_weight', ascending=False)
