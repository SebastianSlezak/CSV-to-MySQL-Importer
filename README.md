# CSV to Database Importer

This script automates the process of importing CSV files into a MySQL database. It scans a specified folder (and its subfolders) for CSV files, then creates a new table for each CSV file and imports its contents into the corresponding table in a MySQL database.

## Requirements

- Python 3
- pandas
- SQLAlchemy
- A MySQL database

## Installation

Ensure you have the required libraries installed. You can install them using pip:

```
pip install pandas sqlalchemy pymysql
```

## Functions

### `find_csv_files(folder_path)`

Searches for all `.csv` files within a given folder and its subdirectories.

**Parameters:**

- `folder_path`: A string specifying the path to the folder to search.

**Returns:**

- A list of file paths for each `.csv` file found.

### `create_db_table(csv_file, engine)`

Creates a new table in the database for a given CSV file and imports the data.

**Parameters:**

- `csv_file`: The file path of the `.csv` file to be imported.
- `engine`: An SQLAlchemy engine instance connected to the target database.

**Returns:**

- None. The function directly imports data into the database.

## Main Execution

When the script is executed, it prompts the user to enter a folder path. If the path is valid and contains `.csv` files, it connects to a predefined MySQL database using SQLAlchemy and imports each `.csv` file into a new table named after the file (excluding the file extension).

### Database Connection

The script uses SQLAlchemy to connect to a MySQL database. The connection is established using the following line:

Make sure to customize the database connection string in the script (`mysql+pymysql://root:root@localhost/database`) to match your database credentials and the name of your database.

```python
engine = create_engine('mysql+pymysql://root:root@localhost/database')
```

In this connection string:
- `mysql+pymysql`: Specifies the database dialect (`mysql`) and the driver (`pymysql`).
- `root`: The username for your MySQL database (change if your username is different).
- `root`: The password for your MySQL database (change to your actual password).
- `localhost`: The host where your database is running (change if your database is on a remote server).
- `database`: The name of your database. **Replace 'database' with the actual name of your database.**

After configuring the connection string, the script imports each `.csv` file in the specified folder and its subdirectories into the MySQL database, with each file's contents in its own table.

## Example Usage

1. Ensure your MySQL database is running and accessible.
2. Execute the script:
    ```
    python csv_to_db.py
    ```
3. When prompted, enter the path to the folder containing your `.csv` files:
    ```
    Enter the path to the folder: /path/to/your/folder
    ```

After running, each `.csv` file in the specified folder and its subdirectories will be imported into the MySQL database, with each file's contents in its own table.

---

