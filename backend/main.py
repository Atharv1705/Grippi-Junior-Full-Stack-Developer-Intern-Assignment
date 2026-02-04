from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import sqlite3
import os
from contextlib import contextmanager

# Create the FastAPI app
app = FastAPI(title="Campaign Analytics API", version="1.0.0")

# Allow frontend to connect from localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database file path
DATABASE_PATH = "campaigns.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_database():
    """Set up the database with some sample campaign data"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Create the campaigns table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL,
                clicks INTEGER NOT NULL,
                cost REAL NOT NULL,
                impressions INTEGER NOT NULL
            )
        """)
        
        # Only add sample data if table is empty
        cursor.execute("SELECT COUNT(*) FROM campaigns")
        if cursor.fetchone()[0] == 0:
            # Sample data with Indian Rupee equivalent values
            sample_campaigns = [
                ("Summer Sale", "Active", 150, 3799.25, 1000),
                ("Black Friday", "Paused", 320, 7399.50, 2500),
                ("Holiday Special", "Active", 275, 5559.75, 1800),
                ("Spring Launch", "Paused", 89, 1962.25, 650),
                ("Back to School", "Active", 445, 9279.80, 3200),
                ("Valentine's Day", "Paused", 198, 4614.40, 1450),
                ("Easter Promotion", "Active", 167, 3405.20, 1100),
                ("Mother's Day", "Active", 234, 6522.90, 1750),
                ("Father's Day", "Paused", 156, 3178.45, 980),
                ("End of Year", "Active", 389, 7902.60, 2800)
            ]
            
            cursor.executemany(
                "INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES (?, ?, ?, ?, ?)",
                sample_campaigns
            )
            conn.commit()

# Initialize database when app starts
init_database()

@app.get("/")
async def root():
    return {"message": "Campaign Analytics API", "version": "1.0.0"}

@app.get("/campaigns")
async def get_campaigns(status: Optional[str] = Query(None, description="Filter by campaign status (Active/Paused)")):
    """
    Get all campaigns, optionally filtered by status
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Filter by status if provided
            if status:
                cursor.execute("SELECT * FROM campaigns WHERE status = ?", (status,))
            else:
                cursor.execute("SELECT * FROM campaigns")
            
            # Convert rows to dictionaries
            campaigns = []
            for row in cursor.fetchall():
                campaigns.append({
                    "id": row["id"],
                    "name": row["name"],
                    "status": row["status"],
                    "clicks": row["clicks"],
                    "cost": row["cost"],
                    "impressions": row["impressions"]
                })
            
            return {"campaigns": campaigns, "total": len(campaigns)}
    
    except Exception as e:
        return {"error": str(e)}, 500

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)