# Data Engineering Assessment

# **Property Data ETL Process**

This project is designed to extract property-related data from a CSV file, clean and normalize it, and then load it into a MySQL database with the required relational structure.

This document consist of screenshots also : [Link](https://docs.google.com/document/d/1nCsYIPvH7R99JCyOLz8U8RKGF9BSOWehdV6VAC8H_Rg/edit?usp=sharing)

## **1. Database Setup**
Before running the ETL script, you must set up a **MySQL database** and **create the necessary tables**.


### **1.1. Install MySQL**
Ensure that **MySQL** is installed and running. You can download MySQL from [here](https://dev.mysql.com/downloads/).

### **1.2. Create the MySQL Database**
1. Open **MySQL Workbench** and create a new connection:
   ```sql
   CREATE DATABASE home_db;
   ```

### **1.3. Create the Tables**
2. Run the below **SQL script** to create the necessary tables (`property` and `leads`) in the `home_db` database:
   - The **`property`** table contains details about the property.
   - The **`leads`** table contains details about leads and references the `property` table via `property_id`.

**SQL code to create the tables:**
```sql
-- Create property table
CREATE TABLE IF NOT EXISTS property (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    Property_Title VARCHAR(255),
    Address VARCHAR(255),
    Latitude DECIMAL(9, 6),
    Longitude DECIMAL(9, 6),
    Street_Address VARCHAR(255),
    City VARCHAR(255),
    State VARCHAR(255),
    Zip_Code VARCHAR(10),
    Redfin_Value DECIMAL(15, 2),
    Taxes INT,
    Subdivision VARCHAR(255)
);

-- Create leads table
CREATE TABLE IF NOT EXISTS leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,  -- Foreign Key reference to property
    Reviewed_Status VARCHAR(255),
    Most_Recent_Status VARCHAR(255),
    Source VARCHAR(255),
    Market VARCHAR(255),
    Occupancy VARCHAR(255),
    Flood VARCHAR(255),
    Selling_Reason VARCHAR(255),
    HOA_Flag VARCHAR(255),
    Final_Reviewer VARCHAR(255),
    School_Average DECIMAL(4, 2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);
```

### **1.4. Configure Database Connection**
Update the **database connection credentials** in the Python ETL script (`etl_script.py`) to match your MySQL configuration. The connection parameters look like this:
```python
connection = mysql.connector.connect(
    host='localhost',   
    database='home_db',  
    user='db_user',  
    password='6equj5_db_user'  
)
```

### **1.5. Ensure MySQL is Running**
 use MySQL Workbench to connect to your database.

---

## **2. Dependencies**
The Python ETL script requires the following Python libraries:
- **pandas**: For data manipulation and reading the CSV file.
- **mysql-connector-python**: To interact with MySQL.

### **Install Dependencies**
To install the required dependencies, run the following command:
```bash
pip install pandas mysql-connector-python
```

---

## **3. Running the ETL Script**
The **ETL script** will:
1. **Read** data from the initial CSV file (`fake_data.csv`).
2. **Clean** and **normalize** the data (handle missing values, whitespace, etc.).
3. **Insert** the cleaned data into the **MySQL database** (`home_db`) in the appropriate tables.

### **3.1. Prepare the CSV File**
Ensure the CSV file (`fake_data.csv`) is available in the project folder and properly formatted.

### **3.2. Edit the ETL Script (if needed)**
- Open the **ETL script** (`etl.py`).
- **Specify the correct file path** for your CSV file in the `etl()` function call:
  ```python
  etl('F:\\HomeLLC assessment\\data_engineer_assessment\\sql\\fake_data.csv')  # this one is mine path location, change it to yours
  ```

### **3.3. Run the ETL Script**
To run the ETL process, open your terminal or command prompt and execute the following command:
```bash
python scripts/etl_script.py
```
This command will:
- Read the **CSV file**,
- **Clean** and **transform** the data,
- **Load** it into the `home_db` MySQL database.

### **3.4. Verify the Data in MySQL**
After running the ETL script, check the data by running the following queries in MySQL:
```sql
-- Check the first 10 rows of the property table
SELECT * FROM property;

-- Check the first 10 rows of the leads table
SELECT * FROM leads;
```



You should see the **normalized** data inserted into the `property` and `leads` tables.

---

## **4. Troubleshooting**
If you encounter issues, here are a few common troubleshooting steps:

1. **MySQL Connection Issues**:
   - Ensure that MySQL is running.
   - Check that the **host**, **database**, **user**, and **password** in the connection string are correct.

2. **Missing Dependencies**:
   - If you get errors related to missing libraries, install the required dependencies using:
     ```bash
     pip install pandas mysql-connector-python
     ```

3. **CSV Formatting Issues**:
   - Verify that the CSV is formatted correctly, with appropriate columns (e.g., `Property_Title`, `Address`, etc.) and no additional empty rows.

---

## **5. Conclusion**
This project provides a full **ETL process** to read, clean, transform, and load property-related data into a **normalized MySQL database**. By following the steps in this documentation, you can easily set up, run, and verify the ETL process.

---

