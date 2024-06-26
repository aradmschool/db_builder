import pandas as pd

def parse_schema(file_path):
    '''convert table schema to dict - table schema row order matters'''
    schema_df = pd.read_csv(file_path)

    # validate columns
    expected_cols = ['table', 'column', 'data_type', 'primary_key', 'foreign_key']
    if not all(col in schema_df.columns for col in expected_cols):
        raise ValueError("missing required columns in schema.csv")
    
    # make dictionary
    schema = {}
    for _, row in schema_df.iterrows():
        table = row['table']
        if table not in schema:
            schema[table] = []
        schema[table].append(row)

    return schema
