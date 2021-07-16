import numpy as np
import pandas as pd
import time

from helpers import clone_drop_and_convert, clone_impute_data, perf_measures, round_decision, reduce_dataframe_using_min_non_null, get_coefficent_weights
from models import apply_linear_regression_model

def predict_country (rowset_label, columnset_label, imputed_df, cutoffs, country_to_classify, row_sample_rate):
    is_country = lambda country: 1 if country == country_to_classify else 0

    results = []
    for cutoff in cutoffs:
        reduced_x = reduce_dataframe_using_min_non_null(imputed_df, cutoff)
        X_columns = [ elem for elem in reduced_x.columns if elem not in ['Country']]

        start = time.time()
        X = reduced_x[X_columns]
        y = reduced_x['Country'].map(is_country)
        metrics, model = apply_linear_regression_model(X, y)

        metrics['country'] = country_to_classify
        metrics['coefficients'] = get_coefficent_weights(model.coef_, X_columns)
        metrics['model'] = model
        metrics['cutoff'] = cutoff
        metrics['X_columns'] = X_columns
        metrics['column_count'] = len(X_columns)
        metrics['rowset_label'] = rowset_label
        metrics['columnset_label'] = columnset_label
        metrics['row_sample_rate'] = row_sample_rate
        metrics['duration'] = round(1000 * (time.time() - start),3)
        results.append(metrics)

        print("rowset_label=%s, columnset_label=%s, cutoff=%s yield columns=%s, ACC=%s, in duration=%ss" % (rowset_label, columnset_label, cutoff, len(X_columns), metrics['ACC'], metrics['duration']))

    return results