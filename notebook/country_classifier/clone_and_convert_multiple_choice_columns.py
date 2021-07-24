import pandas as pd

from country_classifier.convert_multiple_choice_to_dataframe import convert_multiple_choice_to_dataframe

def clone_and_convert_multiple_choice_columns (input_df):
    df = input_df.copy()
    
    multiple_choice_columns = [
        'DatabaseDesireNextYear',
        'DatabaseWorkedWith',
        'DevType',
        'EdLevel',
        'Employment',
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