import pandas as pd
import numpy as np

def clone_drop_and_convert (input_df):
    '''
    INPUT:
    X - dataframe - model inputs
    y - series - binary to indicate if this response is from country or not

    OUTPUT:
    metrics - performance metrics about the model
    model - the trained model
    model_type - string - identifies the model type

    Perform some data transforms
      * set the Respondent id as the index
      * drop some currency columns that are processed into a better representation
      * drop some columns that would directly predict the country
      * convert the "nearly numeric" series to numeric
    '''

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

def _convert_age_series_to_numeric (input_string):
    '''
    INPUT:
    input_string - either a number of a string inequality statement

    OUTPUT:
    number - the input converted to an int

    convert the "nearly numeric" survey responses into numerics, with a slight loss of accuracy in how i choose to process inequalities
    '''

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
