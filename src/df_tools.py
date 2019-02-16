import pandas as pd


def calculate_df_percentage_by_row(df):
    new_df = {}
    for i, row in df.iterrows():
        new_df[i] = row*100/row.sum()

    return pd.DataFrame(new_df)


def calculate_df_percentage_by_row(df):
    new_df = {}
    for i, row in df.iterrows():
        new_df[i] = row*100/row.sum()

    return pd.DataFrame(new_df)
