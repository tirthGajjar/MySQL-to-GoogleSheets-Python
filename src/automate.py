import mysql.connector
from save_to_spreadsheet import authenticate, create_tab, write_data
import datetime

def getSheetName():
    # TO-DO (Optional)
    # Remove below lines and write your own logic to create a sheet with different name
    now = datetime.datetime.now()
    today = now.strftime("%d %b %Y")
    return today


def getData():
    # TO-DO
    # Enter your database connection details here
    # Keep the ssl_disabled = "True" if you are facing any issue
    sh_db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="",
        ssl_disabled="True",
    )

    db_cursor = sh_db.cursor()

    # TO-DO
    # Paste your query here
    # Replace YOUR QUERY GOES HERE with your query, DO NOT REMOVE THE """ """
    db_cursor.execute(""" YOUR QUERY GOES HERE """)

    # TO-DO
    # Enter your column names as 2-d list 
    # Replace column name 1, 2 etc with your column names
    # These names will be saved as column titles in your Google Sheet 
    data = [
        [
            "Column name 1",
            "Column name 2",
            "Column name 3"
        ]
    ]

    result = db_cursor.fetchall()
    data += result
    return data


def main():
    # TO-DO
    # Enter the ID of the Google Spreadsheet in which we are going to save the data
    # Make sure that the authenticated account has access to this Google Sheet
    SPREADSHEET_ID = "ID OF YOUR SPREAD SHEET (GET IT FROM URL)"
    SHEET_NAME = getSheetName()
    SERVICE = authenticate()
    DATA = getData()
    create_tab(SERVICE, SPREADSHEET_ID, SHEET_NAME)
    write_data(SERVICE, SPREADSHEET_ID, SHEET_NAME, DATA)

if __name__ == "__main__":
    main()
