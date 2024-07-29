import pandas as pd
from logger_custom import app_logger
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


# Get the environment variables and connect to PG DB
def connect_to_pgdb(db_conn: dict) -> object:
    """
    The function `connect_to_pgdb` establishes a connection to a PostgreSQL database using environment
    variables for credentials and database information.

    :param db_name: The `db_name` parameter in the `connect_to_pgdb` function is used to specify the
    name of the PostgreSQL database to connect to. If no `db_name` is provided when calling the
    function, it will attempt to retrieve the database name from the environment variables
    :return: An SQLAlchemy engine object is being returned from the `connect_to_pgdb` function.
    """
    # Getting environment variables
    db_username, db_pwd, db_host, db_port, db_name = db_conn.values()

    app_logger.info("--> Initialize connection to PG DB")

    if not all([db_username, db_pwd, db_host, db_name]):
        raise ValueError("Database connection details are not fully specified.")

    # Create an engine instance
    con_string = f"""postgresql://{db_username}:{
            db_pwd}@{db_host}:{db_port}/{db_name}"""

    engine = create_engine(url=con_string, echo=True)
    # logger.debug(engine)

    return engine


# Write data into 'jobs' table in PG DB
def write_df_to_db(engine: object, df: pd.DataFrame, table_name: str) -> None:
    """
    The function `write_df_to_db` writes a DataFrame to a specified table in a PostgreSQL database using
    the provided engine.

    :param engine: The `engine` parameter in the `write_df_to_db` function is typically an SQLAlchemy
    engine object that represents a connection to a database. It is used to establish a connection to
    the database where you want to write the DataFrame (`df`) data
    :param df: The `df` parameter in the `write_df_to_db` function is a pandas DataFrame containing
    weather data that you want to write to a PostgreSQL database table
    :param table_name: The `table_name` parameter in the `write_df_to_db` function is a string that
    represents the name of the table in the PostgreSQL database where the data from the DataFrame (`df`)
    will be written to
    :return: The function `write_df_to_db` is returning a debug log message indicating whether the data
    has been successfully written into the specified table in the PostgreSQL database or if an error
    occurred during the process.
    """
    # write function name to log
    app_logger.info("Starting function write_df_to_db()")
    if not isinstance(engine, Engine):
        app_logger.error("Provided engine is not an instance of SQLAlchemy Engine.")
        return

    try:
        app_logger.debug("--> Starting writing weather data in PG DB")
        # Write data into 'jobs' table in PG DB
        df.to_sql(table_name, engine, if_exists="append", index=False)
        message = "Data into PG DB table has been written."

    except Exception as e:
        app_logger.error(f"Error: {e}")
        message = f"Error: {e}"

    return app_logger.debug(message)


def write_df_to_db2(
    engine: object,
    df: pd.DataFrame,
    table_name: str,
    if_exists: str = "append",
    dtype: dict = None,
) -> None:
    """
    The function `write_df_to_db2` writes a DataFrame to a specified table in a PostgreSQL database using
    the provided engine.

    :param engine: The `engine` parameter in the `write_df_to_db2` function is typically an SQLAlchemy
    engine object that represents a connection to a database. It is used to establish a connection to
    the database where you want to write the DataFrame (`df`) data
    :param df: The `df` parameter in the `write_df_to_db2` function is a pandas DataFrame containing
    weather data that you want to write to a PostgreSQL database table
    :param table_name: The `table_name` parameter in the `write_df_to_db2` function is a string that
    represents the name of the table in the PostgreSQL database where the data from the DataFrame (`df`)
    will be written to
    :param if_exists: The `if_exists` parameter in the `write_df_to_db2` function is a string that
    specifies how to behave if the table already exists in the database. The default value is "append",
    which means that the DataFrame will be appended to the existing table. Other possible values are
    "fail" (raise an error if the table already exists) and "replace" (replace the existing table with
    the DataFrame)
    :param dtype: The `dtype` parameter in the `write_df_to_db2` function is an optional dictionary
    that specifies the data types of the columns in the table. The keys of the dictionary should be the
    column names and the values should be the corresponding data types. If not provided, the data types
    will be inferred from the DataFrame
    :return: The function `write_df_to_db2` is returning a debug log message indicating whether the data
    has been successfully written into the specified table in the PostgreSQL database or if an error
    occurred during the process.
    """
    # write function name to log
    app_logger.info("Starting function write_df_to_db2()")
    if not isinstance(engine, Engine):
        app_logger.error("Provided engine is not an instance of SQLAlchemy Engine.")
        return

    try:
        app_logger.debug("--> Starting writing weather data in PG DB")
        # Write data into 'jobs' table in PG DB
        df.to_sql(table_name, engine, if_exists=if_exists, index=False, dtype=dtype)
        message = "Data into PG DB table has been written."

    except Exception as e:
        app_logger.error(f"Error: {e}")
        message = f"Error: {e}"

    return app_logger.debug(message)
