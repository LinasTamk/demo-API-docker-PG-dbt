import json
import os
import subprocess
import argparse
from dotenv import load_dotenv

from get_kaggle_csv import main_kaggle, get_kaggle_csv
from load_csv_to_pgdb import csv_to_df_to_pgdb
from logger_custom import app_logger
from db_functions import connect_to_pgdb


def run_dbt_command(command, working_dir):
    """
    The `run_dbt_command` function executes a given command using subprocess in Python and prints the
    output or error message accordingly.

    :param command: The `run_dbt_command` function you provided is designed to run a command using the
    `subprocess` module in Python. It captures the output of the command and prints it if the command is
    executed successfully. If an error occurs during command execution, it catches the
    `CalledProcessError` exception
    """
    try:
        result = subprocess.run(
            command, cwd=working_dir, shell=True, text=True, capture_output=True
        )
        app_logger.info(f"Command '{command}' executed successfully.")
        app_logger.info(f"Output:\n {result.stdout}")
    except subprocess.CalledProcessError as e:
        app_logger.info(f"Error executing command '{command}': {e}")
        app_logger.info(f"Error Output:\n {e.stderr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the main script with arguments.")
    parser.add_argument("--dbt_command", required=False, help="DBT command to run.")
    parser.add_argument("--load_raw", required=False, help="Load raw data into PostgreSQL.")
    
    args = parser.parse_args()
    
    app_logger.info(f"Working dir is => {os.getcwd()}")
    # Load environment variables from .env file
    load_dotenv()

    kaggle_csv_file_path = os.getenv("KAGGLE_CSV_FILE_PATH")
    kaggle_csv_file_renamed_path = os.getenv("KAGGLE_CSV_FILE_RENAMED_PATH")
    
    # Define PostgreSQL database connection variables into a dictionary
    pgdb_conn_vars = {
        "db_username": os.getenv("PG_DB_USER"),
        "db_pwd": os.getenv("PG_DB_PASSWORD"),
        "db_host": os.getenv("PG_DB_HOST"),
        "db_port": os.getenv("PG_DB_PROT"),
        "db_name": os.getenv("PG_DB_NAME"),
    }
    
    # Check if argument is provided to load raw data into PostgreSQL
    if args.load_raw == "True" or args.load_raw == "true" or args.load_raw == "1" or args.load_raw == "Y" or args.load_raw == "y":
        # Call the main function with parameters to donwload the Kaggle CSV file and rename it
        get_kaggle_csv()
        main_kaggle(rename=True, src=kaggle_csv_file_path, dst=kaggle_csv_file_renamed_path)

        # Create SQLAlchemy engine
        engine = connect_to_pgdb(pgdb_conn_vars)

        # Load the renamed CSV file into a PostgreSQL database table
        csv_to_df_to_pgdb(engine, kaggle_csv_file_renamed_path)

    # Define the working directory for the dbt project
    working_dir = "/user/app/dbt"

    # Define your dbt commands
    if args.dbt_command:
        dbt_commands = [args.dbt_command]
    else:
        dbt_commands = ["dbt deps", "dbt run", "dbt test"]

    # Run the dbt commands
    for command in dbt_commands:
        run_dbt_command(command, working_dir)
