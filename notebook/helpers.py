def convert_age_series_to_numeric (input_string):
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