import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection function
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='home_db',  # The database you created
            user='db_user',  # MySQL username
            password='6equj5_db_user'  # MySQL password
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# ETL Process
def etl(csv_file):
    # Step 1: Extract data from CSV file
    df = pd.read_csv(csv_file)
    print("CSV Data Loaded")

    # Step 2: Handle NaN and empty string values by replacing them with default values
    # Replace NaN with None (MySQL will interpret this as NULL)
    df = df.fillna({
        'Reviewed_Status': 'Unknown',
        'Most_Recent_Status': 'Unknown',
        'Source': 'Unknown',
        'Market': 'Unknown',
        'Occupancy': 'Unknown',
        'Flood': 'Unknown',
        'Selling_Reason': 'Unknown',
        'HOA_Flag': 'No',
        'Final_Reviewer': 'Unknown',
        'School_Average': 0  # For numeric columns
    })

    # Strip whitespace and replace blank-like values with 'Unknown'
    text_columns = ['Reviewed_Status', 'Most_Recent_Status', 'Source', 'Market', 
                    'Occupancy', 'Flood', 'Selling_Reason', 'HOA_Flag', 'Final_Reviewer']

    for col in text_columns:
        # Strip whitespace from the text column
        df[col] = df[col].astype(str).str.strip()  # Remove leading/trailing spaces
        # Replace empty strings, None, NaN, and NULL strings with "Unknown"
        df[col] = df[col].replace(["", "None", "nan", "NaN", "NULL"], "Unknown")

    # For numeric columns like School_Average, coerce errors to NaN and replace with 0
    df['School_Average'] = pd.to_numeric(df['School_Average'], errors='coerce').fillna(0)

    # Step 3: Transform and load data into the database
    connection = connect_db()
    if connection:
        cursor = connection.cursor()

        # Insert property data into the property table
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO property (Property_Title, Address, Latitude, Longitude, 
                                      Street_Address, City, State, Zip, Redfin_Value, 
                                      Taxes, Subdivision) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['Property_Title'], row['Address'], row['Latitude'], row['Longitude'], 
                row['Street_Address'], row['City'], row['State'], row['Zip'], 
                row['Redfin_Value'], row['Taxes'], row['Subdivision']
            ))
            property_id = cursor.lastrowid  # Get the last inserted property_id

            # Insert leads data
            cursor.execute("""
                INSERT INTO leads (property_id, Reviewed_Status, Most_Recent_Status, 
                                   Source, Market, Occupancy, Flood, Selling_Reason, 
                                   HOA_Flag, Final_Reviewer, School_Average)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                property_id, row['Reviewed_Status'], row['Most_Recent_Status'], 
                row['Source'], row['Market'], row['Occupancy'], row['Flood'], 
                row['Selling_Reason'], row['HOA_Flag'], row['Final_Reviewer'], 
                row['School_Average']
            ))

        connection.commit()
        print("Data inserted successfully")
        cursor.close()
        connection.close()

# Run the ETL process
if __name__ == "__main__":
    etl('F:\\HomeLLC assessment\\data_engineer_assessment\\sql\\fake_data.csv')  # Replace with the actual path to your CSV file
