import pandas as pd

def clean_duplicates(dataframe, column_name='visit_id'):
    dataframe_sorted = dataframe.sort_values(by='date_time')
    dataframe_cleaned = dataframe_sorted.drop_duplicates(subset=[column_name], keep='first')
    return dataframe_cleaned

def clean_nan_variations(dataframe, column_name='Variation'):
    dataframe_cleaned = dataframe.dropna(subset=[column_name])
    return dataframe_cleaned

def split_dataframe_by_variation(dataframe, column_name='Variation'):
    unique_values = dataframe[column_name].unique()
    return {value: dataframe[dataframe[column_name] == value] for value in unique_values}

def check_for_duplicates(dataframe):
    duplicates = dataframe.duplicated(keep=False)
    return duplicates.sum()

def calculate_error_rate(df, step_order):
    df_sorted = df.sort_values(by=['client_id', 'date_time'])

    df_sorted['process_step_order'] = df_sorted['process_step'].map(step_order)
    
    df_sorted['prev_step_order'] = df_sorted.groupby('client_id')['process_step_order'].shift(1)
    
    df_sorted['is_error'] = df_sorted.apply(
        lambda row: row['prev_step_order'] > row['process_step_order'] if pd.notna(row['prev_step_order']) else False, 
        axis=1
    )

    total_errors = df_sorted['is_error'].sum()
    total_steps = df_sorted.shape[0]
    
    error_rate = total_errors / total_steps
    return error_rate
