def remove_outliers(df, columns, z_threshold=3):
    from scipy import stats
    z_scores = stats.zscore(df[columns])
    return df[(abs(z_scores) < z_threshold).all(axis=1)]