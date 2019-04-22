import mysql.connector
from save_to_spreadsheet import authenticate, create_tab, write_data
import datetime


def getSheetName():
    now = datetime.datetime.now()
    today = now.strftime("%d %b %Y")
    return today


def getData():
    sh_db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="",
        ssl_disabled="",
    )

    db_cursor = sh_db.cursor()

    db_cursor.execute(""" YOUR QUERY GOES HERE """)

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
    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = "ID OF YOUR SPREAD SHEET (GET IT FROM URL)"
    SHEET_NAME = getSheetName()
    SERVICE = authenticate()
    DATA = getData()
    create_tab(SERVICE, SPREADSHEET_ID, SHEET_NAME)
    write_data(SERVICE, SPREADSHEET_ID, SHEET_NAME, DATA)


if __name__ == "__main__":
    main()
