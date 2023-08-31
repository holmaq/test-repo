import duckdb


#duckdb.sql("describe Select * from shopify.csv")

duckdb.sql("select Date, Data_origin_identifier as DataOrigin, Total_Sales_GBP from read_csv_auto('Shopify_20220101_20220118.csv', normalize_names=True) \
            WHERE Product_Type='Period Pants' \
           AND Sale_Line_Type = 'PRODUCT' \
           AND Order_ID = 4377125093544 \
           ORDER BY Date DESC").show()

