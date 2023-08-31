import duckdb
import pandas as pd
import great_expectations as gx
#from great_expectations import Checkpoint

#df = duckdb.sql("SELECT * FROM read_csv_auto('Shopify_20220101_20220118.csv', normalize_names=True)").df()

gx_root_dir = 'Great_Expectations/'
ctx = gx.get_context(context_root_dir=gx_root_dir)


ctx.list_expectation_suite_names()

