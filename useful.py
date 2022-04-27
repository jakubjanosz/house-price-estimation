import pandas as pd
import numpy as np

# removing values in 'price_per_m2' column that are more than 3 standard deviations from mean
def remove_outliers_per(df):
    df_result = pd.DataFrame()
    for key, subdf in df.groupby('city'):
        m = np.mean(subdf.price_per_m2)
        sd = np.std(subdf.price_per_m2)
        reduced_df = subdf[(subdf.price_per_m2 > (m - sd)) & (subdf.price_per_m2 <= (m + sd))]
        df_result = pd.concat([df_result, reduced_df], ignore_index=True)
    return df_result


def remove_outliers_p(df):
    df_result = pd.DataFrame()
    for key, subdf in df.groupby('city'):
        m = np.mean(subdf.price)
        sd = np.std(subdf.price)
        reduced_df = subdf[(subdf.price > (m - 3 * sd)) & (subdf.price <= (m + 3 * sd))]
        df_result = pd.concat([df_result, reduced_df], ignore_index=True)
    return df_result


def remove_outliers_s(df):
    df_result = pd.DataFrame()
    for key, subdf in df.groupby('city'):
        m = np.mean(subdf.sq)
        sd = np.std(subdf.sq)
        reduced_df = subdf[(subdf.sq > (m - 3 * sd)) & (subdf.sq <= (m + 3 * sd))]
        df_result = pd.concat([df_result, reduced_df], ignore_index=True)
    return df_result


# removing values in 'year' column that are more than 3 standard deviations from mean
def remove_outliers_y(df):
    df_result = pd.DataFrame()
    for key, subdf in df.groupby('city'):
        m = np.mean(subdf.year)
        sd = np.std(subdf.year)
        reduced_df = subdf[(subdf.year > (m - 3 * sd)) & (subdf.year <= (m + 3 * sd))]
        df_result = pd.concat([df_result, reduced_df], ignore_index=True)
    return df_result