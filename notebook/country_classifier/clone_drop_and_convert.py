import pandas as pd
import numpy as np

from country_classifier.convert_multiple_choice_to_dataframe import convert_multiple_choice_to_dataframe

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

def clone_drop_and_convert (input_df):
    df = input_df.copy()
    
    # use respondent as the index
    if 'Respondent' in df.columns:    
        df.set_index('Respondent')

    # Exclude CompTotal and CompFreq as they are free form and not in a standard currency, use ConvertedComp which is normalised to annual USD
    for raw_compensation_column in ['CompTotal', 'CompFreq']:
        if raw_compensation_column in df.columns:
            df.drop(columns=[raw_compensation_column], inplace=True)

    # Exclude columns that would obviously directly correlate with country of origin
    for unfair_predictors in ['CurrencyDesc', 'CurrencySymbol', 'Ethnicity']:
        if unfair_predictors in df.columns:
            df.drop(columns=[unfair_predictors], inplace=True)

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