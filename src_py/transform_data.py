import pandas as pd


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    The function `rename_columns` renames the columns of a DataFrame by removing underscores and
    inserting underscores before capital letters.

    :param df: The `rename_columns` function takes a DataFrame as input and performs the following
    operations on its column names:
    :return: The function `rename_columns` takes a DataFrame `df`, removes underscores from column
    names, adds underscores before capital letters, and converts all column names to lowercase. The
    function returns the modified DataFrame `df`.
    """
    df.columns = df.columns.str.replace("_", "", regex=True)
    df.columns = df.columns.str.replace("\\B([A-Z]+)", "_\\1", regex=True)
    df.columns = [x.lower() for x in df.columns]

    return df
