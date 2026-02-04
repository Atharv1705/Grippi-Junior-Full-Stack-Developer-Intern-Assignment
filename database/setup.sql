-- Grippi Campaign Analytics Database Setup
-- PostgreSQL version

-- Create campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Active', 'Paused')),
    clicks INTEGER NOT NULL DEFAULT 0,
    cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    impressions INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample campaign data with Indian Rupee values
INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale', 'Active', 150, 3799.25, 1000),
('Black Friday', 'Paused', 320, 7399.50, 2500),
('Holiday Special', 'Active', 275, 5559.75, 1800),
('Spring Launch', 'Paused', 89, 1962.25, 650),
('Back to School', 'Active', 445, 9279.80, 3200),
('Valentine''s Day', 'Paused', 198, 4614.40, 1450),
('Easter Promotion', 'Active', 167, 3405.20, 1100),
('Mother''s Day', 'Active', 234, 6522.90, 1750),
('Father''s Day', 'Paused', 156, 3178.45, 980),
('End of Year', 'Active', 389, 7902.60, 2800);

-- Create index for better query performance
CREATE INDEX IF NOT EXISTS idx_campaigns_status ON campaigns(status);

-- Verify data insertion
SELECT COUNT(*) as total_campaigns FROM campaigns;
SELECT status, COUNT(*) as count FROM campaigns GROUP BY status;