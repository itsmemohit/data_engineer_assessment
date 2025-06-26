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
    Zip VARCHAR(10),
    Redfin_Value DECIMAL(15, 2),
    Taxes INT,
    Subdivision VARCHAR(255)
);

-- Create leads table
CREATE TABLE IF NOT EXISTS leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
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
