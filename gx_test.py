import duckdb
import pandas as pd
import great_expectations as gx
from great_expectations import Checkpoint

df = duckdb.sql("SELECT * FROM read_csv_auto('Shopify_20220101_20220118.csv', normalize_names=True)").df()

gx_root_dir = 'Great_Expectations/'
ctx = gx.get_context(context_root_dir=gx_root_dir)

df_datasource = ctx.sources.add_or_update_pandas(
    name='pandas_df'
)

df_asset = df_datasource.add_dataframe_asset(
    name='shopify_orders',
    dataframe=df
)

batch_request = df_asset.build_batch_request()

#Expec suite
expectation_suite_name = 'shopify_orders_suite'
ctx.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)

ctx.add_ep

#Create validator
validator = ctx.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
)

validator.expect_column_values_to_not_be_null(column='product_type')
validator.expect_column_values_to_be_between(
    column="total_discount_amount_excluding_taxes_gbp", min_value=0, max_value=100
)

validator.save_expectation_suite(discard_failed_expectations=False)

#Create Checkpoint
checkpoint_name = 'shopify_order_checkpoint'

checkpoint = ctx.add_or_update_checkpoint(name=checkpoint_name, validator=validator)

checkpoint_result = checkpoint.run()

#ctx.view_validation_result(checkpoint_result)