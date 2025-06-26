-- Insert sample data into the property table
INSERT INTO property (Property_Title, Address, Latitude, Longitude, Street_Address, City, State, Zip_Code, Redfin_Value, Taxes, Subdivision) 
VALUES 
('Sample Property 1', '123 Main St', 40.7128, -74.0060, '123 Main St', 'New York', 'NY', '10001', 500000.00, 5000, 'Suburban');

-- Insert sample data into the leads table
INSERT INTO leads (property_id, Reviewed_Status, Most_Recent_Status, Source, Market, Occupancy, Flood, Selling_Reason, HOA_Flag, Final_Reviewer, School_Average)
VALUES
(1, 'Reviewed', 'Pending', 'Online', 'Urban', 'Occupied', 'No', 'Relocation', 'Yes', 'John Doe', 4.5);
