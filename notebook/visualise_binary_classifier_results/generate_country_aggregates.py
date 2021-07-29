import pandas as pd

def generate_country_aggregates (runs_for_country):
    '''
    INPUT:
    runs_for_country - dataframe - the model results for a country

    OUTPUT:
    series containing statistics about the model results for the country

    compute some statistics for display on the model results for each country
    '''

    model_count = runs_for_country.shape[0]
    naive_classifier_count =  runs_for_country.query('TP == 0 and FP == 0').shape[0]
    proportion_of_naive_classifier = round(naive_classifier_count / model_count, 3)
    country_proportion = round(runs_for_country.iloc[0]['P'] / (runs_for_country.iloc[0]['P'] + runs_for_country.iloc[0]['N']),3)

    result = pd.Series({
        'model_count' : model_count,
        'country_proportion': country_proportion,
        'naive_classifier_count' : naive_classifier_count,
        'proportion_of_naive_classifier' : proportion_of_naive_classifier,
    })
    
    return result