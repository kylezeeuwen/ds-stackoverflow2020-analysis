import pandas as pd


def clone_and_convert_multiple_choice_columns(input_df):
    '''
    INPUT:
    input_df - dataframe - survey responses

    OUTPUT:
    dataframe - survey responses with conversion described below

    convert all the "a;b;d" style survey responses to dummied columns
    '''

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
        df = df.merge(dummied_df, how='inner', left_index=True,
                      right_index=True, validate='1:1')

    df.drop(columns=multiple_choice_columns, inplace=True)

    return df


def convert_multiple_choice_to_dataframe(mc_series):
    '''
    INPUT:
    mc_series - series<string> - the answers to a "choose all answers the apply" question, where each answer is seperated by a ';'

    OUTPUT:
    dataframe - one series per distinct answer, values are 0 or 1, adding a 'noresponse' series as well

    take a set of "a;b;d" style survey responses and convert to a DF with (a,b,c,d,noresponse) columns
    '''

    series_name = mc_series.name
    answers_lookup = {}

    def column_name(answer): return '%s_%s' % (series_name, answer)

    def fill_answers_lookup(answer_string):
        answers = [] if answer_string != answer_string else answer_string.split(
            ';')
        for answer in answers:
            if answer not in answers_lookup:
                answers_lookup[answer] = 0
            answers_lookup[answer] += 1
    mc_series.apply(fill_answers_lookup)

    df = pd.DataFrame(index=mc_series.index)
    for answer in answers_lookup.keys():
        df[column_name(answer)] = pd.Series(
            index=mc_series.index, dtype='uint8')
    df[column_name('noresponse')] = pd.Series(
        index=mc_series.index, dtype='uint8')

    def populate_df(answer_string_series):
        index = answer_string_series.name
        value = answer_string_series[0]
        answers = [] if value != value else value.split(';')
        for answer in answers:
            df.at[index, column_name(answer)] = 1

        if value != value:
            df.at[index, column_name('noresponse')] = 1

    mc_series.to_frame(0).apply(populate_df, axis=1)

    return df
