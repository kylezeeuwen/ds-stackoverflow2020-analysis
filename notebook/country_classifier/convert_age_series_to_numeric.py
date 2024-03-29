def convert_age_series_to_numeric(input_string):
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
