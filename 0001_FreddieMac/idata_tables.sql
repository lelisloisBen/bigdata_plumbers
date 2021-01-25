CREATE TABLE BYOL_table1 (
    Region VARCHAR(255),
    Country VARCHAR(255),
    ItemType VARCHAR(255),
    SalesChannel VARCHAR(255),
    OrderPriority VARCHAR(255),
    OrderDate VARCHAR(255),
    OrderID INT NOT NULL,
    ShipDate VARCHAR(255),
    UnitsSold VARCHAR(255),
    UnitPrice VARCHAR(255),
    UnitCost VARCHAR(255),
    TotalRevenue VARCHAR(255),
    TotalCost VARCHAR(255),
    TotalProfit VARCHAR(255),
    PRIMARY KEY (OrderID)
);

CREATE TABLE BYOL_table2 (
    Region VARCHAR(255),
    Country VARCHAR(255),
    ItemType VARCHAR(255),
    SalesChannel VARCHAR(255),
    OrderPriority VARCHAR(255),
    OrderDate VARCHAR(255),
    OrderID INT NOT NULL,
    ShipDate VARCHAR(255),
    UnitsSold VARCHAR(255),
    UnitPrice VARCHAR(255),
    UnitCost VARCHAR(255),
    TotalRevenue VARCHAR(255),
    TotalCost VARCHAR(255),
    TotalProfit VARCHAR(255),
    PRIMARY KEY (OrderID)
);

-- TO LOAD CSV FILE TO A TABLE (MYSQL)
LOAD DATA LOCAL INFILE '/Users/samir/Desktop/BYOL_100SalesRecords.csv' 
INTO TABLE BYOL_table1 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/samir/Desktop/BYOL_5000SalesRecords.csv' 
INTO TABLE BYOL_table2
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- QUERY FOR SPQRK BYOL
SELECT
a.Region,
a.Country,
a.ItemType,
a.SalesChannel,
a.OrderPriority,
a.OrderDate,
a.OrderID,
a.ShipDate,
a.UnitsSold,
a.UnitPrice,
a.UnitCost,
a.TotalRevenue,
a.TotalCost,
a.TotalProfit
FROM BYOL_table1 a JOIN BYOL_table2 b
ON a.ItemType = b.ItemType;