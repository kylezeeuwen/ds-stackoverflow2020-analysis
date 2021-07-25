import pandas as pd


def clone_impute_data(input_df, dummy_na, fill_technique):
    '''
    INPUT:
    input_df - dataframe - survey results
    dummy_na - boolean - binary to indica whether to include a column for N/A
    fill_technique - string - Mean or Mode. Defines which imputation technique to use for numerics

    OUTPUT:
    df - imputed data frame

    Impute data:
      * categorical - convert to dummy columns, optionally including an extra 'no response' column
      * numeric - use either mean or mode
    '''

    df = input_df.copy()
    for column in df.select_dtypes(include='object').columns:
        if column == 'Country':
            continue
        # for each cat add dummy var, drop original column
        df = pd.concat([df.drop(column, axis=1), pd.get_dummies(
            df[column], prefix=column, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)

    def fill_mean(col): return col.fillna(col.mean())
    def fill_mode(col): return col.fillna(col.mode()[0])
    fill = fill_mean if fill_technique == "Mean" else fill_mode

    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        df[column] = fill(df[column])

    return df
