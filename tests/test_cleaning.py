import pandas as pd
from src.data_cleaning import remove_outliers

def test_outlier_removal():
    df = pd.DataFrame({"GHI": [100, 101, 1000]})  # 1000 is an outlier
    cleaned = remove_outliers(df, ["GHI"], z_threshold=2)
    assert len(cleaned) == 2