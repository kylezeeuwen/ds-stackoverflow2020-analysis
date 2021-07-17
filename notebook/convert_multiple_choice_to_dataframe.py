import pandas as pd
import numpy as np

def convert_multiple_choice_to_dataframe (mc_series):
    series_name = mc_series.name
    answers_lookup = {}
    
    column_name = lambda answer: '%s_%s' % (series_name, answer)
    
    def fill_answers_lookup (answer_string):
        answers = [] if answer_string != answer_string else answer_string.split(';')
        for answer in answers:
            if answer not in answers_lookup:
                answers_lookup[answer] = 0
            answers_lookup[answer] += 1    
    mc_series.apply(fill_answers_lookup)
    
    df = pd.DataFrame(index=mc_series.index)
    for answer in answers_lookup.keys():
        df[column_name(answer)] = pd.Series(index=mc_series.index, dtype='uint8')
    df[column_name('noresponse')] = pd.Series(index=mc_series.index, dtype='uint8')
        
    def populate_df (answer_string_series):
        index = answer_string_series.name
        value = answer_string_series[0]
        answers = [] if value != value else value.split(';')
        for answer in answers:
            df.at[index, column_name(answer)] = 1
        
        if value != value:
            df.at[index, column_name('noresponse')] = 1

    mc_series.to_frame(0).apply(populate_df, axis=1)

    return df