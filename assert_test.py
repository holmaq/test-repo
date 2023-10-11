select_column_list = {
            "Col1": ["Col1", "bigint"],
            "Col2": ["Col2", "bigint"],
            "Col3" : ["Col3", "string"],
            "Col4":["Col4", "date"],
            "Col5": ["Col5","string"],
            "Col6": ["Col6", "string"]
        }
        
bigint_cols = [x[0] for x in select_column_list.values() if x[1] == "bigint"]
bigint_sel_str = ','.join(bigint_cols)
