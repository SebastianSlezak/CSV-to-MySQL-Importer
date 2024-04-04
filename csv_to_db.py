import os
import pandas as pd
from sqlalchemy import create_engine
import random

def find_csv_files(folder_path):
    csv_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def create_db_table(csv_file, engine):
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    if os.path.isdir(folder_path):
        csv_files = find_csv_files(folder_path)
        if csv_files:
            engine = create_engine('mysql+pymysql://root:root@localhost/sejm')
            for csv_file in csv_files:
                create_db_table(csv_file, engine)
                print(f"Uploaded CSV file '{csv_file}' to database.")
            print("All CSV files uploaded to the database successfully.")
        else:
            print("No CSV files found in the specified folder and its subfolders.")
    else:
        print("Invalid folder path. Please provide a valid path to a folder.")
