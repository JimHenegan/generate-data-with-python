from ast import literal_eval
from functools import reduce

import pandas as pd


def convert_metadata(md):
  """
  md is a pandas DataFrame that represents the metadata loaded in from a CSV file.
  
  Here, we convert "lists of choices" from the CSV file from strings to lists
  """
  records = []

  for i, row in md.iterrows():
    no_missing = row.dropna()
    as_dict = no_missing.to_dict()
    
    if row['var_dist_type'] == "list_of_choices":     
      list_as_list = literal_eval(row['var_list_of_choices']) 
      as_dict['var_list_of_choices'] = list_as_list
    records.append(as_dict)

  return records


def make_data_frame(converted_metadata, rng, sample_size):        
  list_of_columns = [make_column(record, rng, sample_size) for record in converted_metadata]  
  data_frame = reduce(lambda x, y: x.join(y), list_of_columns)
  return data_frame


def make_column(record, rng, sample_size):
  return pd.DataFrame(get_data(record, rng, sample_size), columns = [record['var_name']])


def get_data(record, rng, sample_size):

  var_dist_type = record['var_dist_type']

  if var_dist_type == "normal":
    mu = record['var_mu']
    sd = record['var_sd']
    return get_sample_from_normal_distribution(rng, mu, sd, sample_size)

  if var_dist_type == "bernoulli":
    p = record['var_p']   
    return get_sample_from_bernoulli_distribution(rng, p, sample_size)

  if var_dist_type == "list_of_choices":
    list_of_choices = record['var_list_of_choices']   
    return get_sample_from_list_of_choices(rng, list_of_choices, sample_size)


def get_sample_from_normal_distribution(rng, mu, sigma, sample_size):
  psuedo_random_numbers = rng.normal(mu, sigma, size = sample_size)
  return psuedo_random_numbers


def get_sample_from_bernoulli_distribution(rng, p, sample_size):
  psuedo_random_numbers = rng.binomial(n=1, p=p, size = sample_size)
  return psuedo_random_numbers


def get_sample_from_list_of_choices(rng, list_of_choices, sample_size):
  psuedo_random_numbers =  rng.choice(list_of_choices, size = sample_size)
  return psuedo_random_numbers