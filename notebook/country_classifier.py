#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install reload')

row_sample_rate = 1


# In[2]:


import numpy as np
import pandas as pd
import time
import reload

from helpers import clone_drop_and_convert, clone_impute_data, perf_measures, round_decision, reduce_dataframe_using_min_non_null, get_coefficent_weights
from models import apply_linear_regression_model
from predict_country import predict_country

# Developer note: If you modify the modules above, the changes to those modules will not be reflected until you 
# re-execute this cell, specifically the reload commands
# TODO this doesn't work yet
# reload(clone_drop_and_convert)
# reload(models)

DUMMY_NA = True
FILL="Mean"

pd.options.display.max_rows = 2000
pd.options.display.max_columns = 1000
pd.options.display.max_colwidth = 255

script_start = time.time()

raw_df = pd.read_csv('./assets/survey_results_public.csv')
schema = pd.read_csv('./assets/survey_results_schema.csv')


# In[3]:


df = clone_drop_and_convert(raw_df)

full_country = df.sample(frac=row_sample_rate, axis=0)
full_country.shape
# (6446, 57)

start = time.time()
full_country_imputed = clone_impute_data(full_country, dummy_na=True, fill_technique=FILL)
end = time.time()
print('full_country impute time %s', end - start)
print("full country dataset has %s rows and %s columns" % (full_country_imputed.shape[0], full_country_imputed.shape[1]))


# In[4]:


countries = full_country['Country'].value_counts()
countries_with_enough_samples = countries[countries > (1000 * row_sample_rate)].index.values
countries_with_enough_samples


# In[5]:


#cutoffs here pertains to the number of missing values allowed in the used columns.
#Therefore, lower values for the cutoff provides more predictors in the model.

# cutoffs = [5000, 3500, 2500, 1000, 100, 50, 30, 25, 0]
cutoffs = [10000, 5000, 2500, 1000, 500]

results = []
for country in countries_with_enough_samples:
    country_results = predict_country(         dataset_name='full_country_%s' % country,         imputed_df=full_country_imputed,         cutoffs=cutoffs,         country_to_classify=country,         row_sample_rate=row_sample_rate     )
    results.extend(country_results)


# In[6]:


result_df = pd.DataFrame(data=results).set_index(['row_label', 'cutoff', 'column_label'])
for to_round in ['TPR', 'TNR', 'PPV', 'NPV', 'ACC', 'duration']:
    result_df[to_round] = result_df[to_round].map(lambda x: round(x,3))

result_df.drop(columns=['X_columns', 'coefficients']).sort_values('ACC')


# In[7]:


script_end = time.time()
print('script duration %s', end - start)


# In[8]:


result_df


# In[ ]:





# In[ ]:




