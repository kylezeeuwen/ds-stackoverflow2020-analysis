import pandas as pd

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
