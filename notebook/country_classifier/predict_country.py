import numpy as np
import pandas as pd
import time

from country_classifier.models import apply_linear_regression_model, apply_linear_svm_model, apply_random_forest_model


def predict_country(rowset_label, columnset_label, imputed_df, cutoffs, country_to_classify, row_sample_rate):
    '''
    INPUT:
    rowset_label - string - label to identify the response subset
    columnset_label - string - label to identify the column set
    imputed_df - dataframe - the cleaned dataframe containing survey results
    cutoffs - array - integer cutoffs to limit input features when building models
    country_to_classify - string - name of country to attempt to identify in the data
    row_sample_rate - float - a sample rate to reduce datasize during testing/development

    OUTPUT:
    results - array - one entry per model, containing fields to identify the model, and model performance results

    Build models to classify survey responses as belonging to a country or not, run the models, and capture performance results
    '''

    def is_country(country): return 1 if country == country_to_classify else 0

    results = []
    for cutoff in cutoffs:
        reduced_x = reduce_dataframe_using_min_non_null(imputed_df, cutoff)
        X_columns = [
            elem for elem in reduced_x.columns if elem not in ['Country']]

        X = reduced_x[X_columns]
        y = reduced_x['Country'].map(is_country)

        start = time.time()
        metrics, model, model_type = apply_linear_regression_model(X, y)
        metrics['country'] = country_to_classify
        metrics['coefficients'] = get_coefficent_weights(
            model.coef_, X_columns)
        metrics['model_type'] = model_type
        metrics['cutoff'] = cutoff
        metrics['X_columns'] = X_columns
        metrics['column_count'] = len(X_columns)
        metrics['rowset_label'] = rowset_label
        metrics['columnset_label'] = columnset_label
        metrics['row_sample_rate'] = row_sample_rate
        metrics['duration'] = round(time.time() - start, 4)
        results.append(metrics)

        print("model_type=%s rowset_label=%s, columnset_label=%s, cutoff=%s yield columns=%s, ACC=%s, in duration=%ss" % (
            metrics['model_type'], rowset_label, columnset_label, cutoff, len(X_columns), metrics['ACC'], metrics['duration']))

        X = reduced_x[X_columns]
        y = reduced_x['Country'].map(is_country)

        start = time.time()
        metrics, model, model_type = apply_random_forest_model(X, y)
        metrics['country'] = country_to_classify
        metrics['coefficients'] = None
        metrics['model_type'] = model_type
        metrics['cutoff'] = cutoff
        metrics['X_columns'] = X_columns
        metrics['column_count'] = len(X_columns)
        metrics['rowset_label'] = rowset_label
        metrics['columnset_label'] = columnset_label
        metrics['row_sample_rate'] = row_sample_rate
        metrics['duration'] = round(time.time() - start, 4)
        results.append(metrics)

        print("model_type=%s rowset_label=%s, columnset_label=%s, cutoff=%s yield columns=%s, ACC=%s, in duration=%ss" % (
            metrics['model_type'], rowset_label, columnset_label, cutoff, len(X_columns), metrics['ACC'], metrics['duration']))

        X = reduced_x[X_columns]
        y = reduced_x['Country'].map(is_country)

        start = time.time()
        metrics, model, model_type = apply_linear_svm_model(X, y)
        metrics['country'] = country_to_classify
        metrics['coefficients'] = None
        metrics['model_type'] = model_type
        metrics['cutoff'] = cutoff
        metrics['X_columns'] = X_columns
        metrics['column_count'] = len(X_columns)
        metrics['rowset_label'] = rowset_label
        metrics['columnset_label'] = columnset_label
        metrics['row_sample_rate'] = row_sample_rate
        metrics['duration'] = round(time.time() - start, 4)
        results.append(metrics)

        print("model_type=%s rowset_label=%s, columnset_label=%s, cutoff=%s yield columns=%s, ACC=%s, in duration=%ss" % (
            metrics['model_type'], rowset_label, columnset_label, cutoff, len(X_columns), metrics['ACC'], metrics['duration']))

    return results

# attribution: function taken from udacity course materials


def get_coefficent_weights(coefficients, columns):
    '''
    INPUT:
    coefficients - the coefficients of the linear model
    columns - the column in the x training set
    OUTPUT:
    coefs_df - a dataframe holding the coefficient, estimate, and abs(estimate)

    Provides a dataframe that can be used to understand the most influential coefficients
    in a linear model by providing the coefficient estimates along with the name of the
    variable attached to the coefficient.
    '''
    coefs_df = pd.DataFrame()
    coefs_df['X_Column'] = columns
    coefs_df['weight'] = coefficients
    coefs_df['abs_weight'] = np.abs(coefficients)
    return coefs_df.sort_values('abs_weight', ascending=False)


def reduce_dataframe_using_min_non_null(input_df, min_non_null_cutoff):
    df = input_df.copy()
    # imprecise as uint8 does not imply a dummied categorical column
    categorical_dummies = df.select_dtypes(include='uint8')
    columns_to_drop = categorical_dummies[categorical_dummies.columns[categorical_dummies.sum(
    ) < min_non_null_cutoff]].columns
    return df.drop(columns=columns_to_drop)
