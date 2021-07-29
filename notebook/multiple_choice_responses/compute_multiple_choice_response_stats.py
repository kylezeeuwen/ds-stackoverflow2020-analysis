import pandas as pd

def compute_multiple_choice_response_stats (df, mc_questions):
    '''
    INPUT:
    df - dataframe - survey responses
    mc_questions - array - list of columns that contain "choose all that apply" survey responses

    OUTPUT:
    question_counts - dataframe - question, question_response_count
    question_answer_counts - dataframe - question, answer, answer_count
    question_counts_by_country - dataframe - question, country, question_response_country_count
    answer_counts_by_country - dataframe - question, answer, country, country_answer_count

    Processes a list of questions from the survey responses.
    Assumes these questions are "choose all that apply" responses, and that the respondents answers are represented as a ';' delimited string.
    Returns aggregrate results in multiple formats.
    '''

    questions_lookup = {}
    questions_country = {}
    answers_by_country = {}

    # term definition vivify: https://en.wikipedia.org/wiki/Autovivification - note this auto-vivification is generally considered to be a bad idea and causes lots of side effects

    # DOCSTRING note: these are all internal fns, input and output will be omitted. For all6 fns:
    #  * INPUT: self documenting strings
    #  * OUTPUT: NONE

    def vivify_question (question):
        '''intialise a record in the questions_lookup dictionary'''

        if question not in questions_lookup:
            questions_lookup[question] = { 'question': question, 'question_response_count': 0 }

    def vivify_questions_country (question, country):
        '''intialise a record in the questions_country dictionary'''

        if (question, country) not in questions_country:
            questions_country[(question, country)] = { 'question': question, 'country': country, 'question_response_country_count': 0 }

    def vivify_answer_by_country (question, answer, country):
        '''intialise a record in the answers_by_country dictionary'''

        if (question, answer, country) not in answers_by_country:
            answers_by_country[(question, answer, country)] = { 'question': question, 'country': country, 'answer': answer, 'country_answer_count': 0 }

    def record_question_was_answered (question, country):
        '''update data structures to record a question response for a given country'''

        vivify_question(question)
        questions_lookup[question]['question_response_count'] +=1
        vivify_questions_country(question, country)
        questions_country[(question, country)]['question_response_country_count'] += 1
        
    def record_answer (question, answer, country):
        '''update data structures to record a question answer for a given country'''

        vivify_answer_by_country(question, answer, country)
        answers_by_country[(question, answer, country)]['country_answer_count'] += 1

    def process_survey_response (response):
        '''update data structures based on the question responses in this survey response'''

        country = response['Country']
        for question in mc_questions:
            answer_string = response[question]
            if answer_string != answer_string:
                None
            else:
                record_question_was_answered(question, country)
                answers = answer_string.split(';')

                for answer in answers:
                    record_answer(question, answer, country)

    df.apply(process_survey_response, axis=1)
    
    question_counts = pd.DataFrame(data=questions_lookup.values())
    question_counts_by_country = pd.DataFrame(data=questions_country.values())
    answer_counts_by_country = pd.DataFrame(data=answers_by_country.values())

    question_answer_counts = answer_counts_by_country \
        .groupby(['question', 'answer']).sum()['country_answer_count'] \
        .reset_index() \
        .rename(columns={"country_answer_count": "answer_count"}) \
        .merge(question_counts, on='question', how='left') \

    question_answer_counts['answer_proportion'] = \
        question_answer_counts['answer_count'] / question_answer_counts['question_response_count']
    question_answer_counts.drop(columns=['question_response_count'], inplace = True)    
    
    return question_counts, question_answer_counts, question_counts_by_country, answer_counts_by_country
