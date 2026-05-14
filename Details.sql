CREATE DATABASE lead_management;
USE lead_management;
CREATE TABLE leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    business_type VARCHAR(100),
    message TEXT,
    status VARCHAR(50) DEFAULT 'New'
);