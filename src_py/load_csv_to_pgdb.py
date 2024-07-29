import json
from pathlib import Path

import pandas as pd
from db_functions import connect_to_pgdb, write_df_to_db2
from logger_custom import app_logger
from sqlalchemy.types import Float, Integer, String
from transform_data import rename_columns
from sqlalchemy.engine.base import Engine


def csv_to_df_to_pgdb(engine: Engine, csv_file_path: Path) -> None:
    """
    The function `csv_to_df_to_pgdb` reads a CSV file into a DataFrame, maps DataFrame data types to
    custom data types, and writes the DataFrame to a PostgreSQL database table.

    :param csv_file_path: The `csv_to_df_to_pgdb` function you provided seems to read data from a CSV
    file, transform it into a DataFrame, map the DataFrame columns to custom data types, and then write
    the DataFrame to a PostgreSQL database table
    :param posgres_db_env_file_path: The `posgres_db_env_file_path` parameter in the `csv_to_df_to_pgdb`
    function refers to the file path where the PostgreSQL database environment variables are stored.
    These variables are typically used for establishing a connection to the PostgreSQL database, such as
    the database URL, username, password, etc
    :return: The function `csv_to_df_to_pgdb` is returning `None`.
    """
    # Load CSV data into a DataFrame
    app_logger.info("Reading CSV file into DataFrame")

    df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")
    app_logger.info("df columns before rename: %s", df.columns)
    df = rename_columns(df)
    app_logger.info("df columns after rename: %s", df.columns)

    # Function to automatically detect data types
    def map_dtype(dtype):
        """
        The function `map_dtype` maps pandas data types to corresponding custom data types Integer, Float,
        or String.

        :param dtype: It looks like the `map_dtype` function is designed to map pandas data types to custom
        data type classes. The function checks if the input `dtype` is an integer type using
        `pd.api.types.is_integer_dtype`, a float type using `pd.api.types.is_float_dtype`, and returns
        corresponding custom
        :return: The `map_dtype` function is returning an instance of a class based on the input `dtype`. If
        the input `dtype` is an integer type, it returns an instance of the `Integer` class. If the input
        `dtype` is a float type, it returns an instance of the `Float` class. Otherwise, it returns an
        instance of the `String` class.
        """
        if pd.api.types.is_integer_dtype(dtype):
            return Integer()
        elif pd.api.types.is_float_dtype(dtype):
            return Float()
        else:
            return String()

    # Map DataFrame dtypes to SQLAlchemy types
    dtype_mapping = {col: map_dtype(df[col].dtype) for col in df.columns}
    app_logger.info(dtype_mapping)
    app_logger.info("Data types mapped successfully!")

    # Write DataFrame to PostgreSQL, automatically creating the table
    write_df_to_db2(
        engine=engine,
        df=df,
        table_name="smarket_raw",
        if_exists="replace",
        dtype=dtype_mapping,
    )

    app_logger.info("Data loaded successfully!")

    return None
