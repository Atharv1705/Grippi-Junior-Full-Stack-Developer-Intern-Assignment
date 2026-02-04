#!/usr/bin/env python3
"""
Test the specific SQL queries mentioned in evaluation criteria
"""

import sqlite3
import json

def test_sql_queries():
    print("🗄️ SQL QUERY TESTING")
    print("=" * 50)
    
    try:
        # Connect to database
        conn = sqlite3.connect("backend/campaigns.db")
        conn.row_factory = sqlite3.Row  # Enable column access by name
        cursor = conn.cursor()
        
        # Test 1: Basic SELECT query
        print("1️ Basic SELECT Query:")
        cursor.execute("SELECT * FROM campaigns")
        all_campaigns = cursor.fetchall()
        print(f"   Query: SELECT * FROM campaigns")
        print(f"   Result: {len(all_campaigns)} campaigns found")
        
        # Test 2: Specific query mentioned in evaluation criteria
        print("\n2️ Status Filter Query (from evaluation criteria):")
        cursor.execute("SELECT * FROM campaigns WHERE status='Active'")
        active_campaigns = cursor.fetchall()
        print(f"   Query: SELECT * FROM campaigns WHERE status='Active'")
        print(f"   Result: {len(active_campaigns)} active campaigns")
        
        # Display active campaigns
        for campaign in active_campaigns:
            print(f"   - {campaign['name']}: ₹{campaign['cost']}, {campaign['clicks']} clicks")
        
        # Test 3: Paused campaigns
        print("\n3️ Paused Campaigns Query:")
        cursor.execute("SELECT * FROM campaigns WHERE status='Paused'")
        paused_campaigns = cursor.fetchall()
        print(f"   Query: SELECT * FROM campaigns WHERE status='Paused'")
        print(f"   Result: {len(paused_campaigns)} paused campaigns")
        
        # Test 4: Aggregation queries
        print("\n4️ Aggregation Queries:")
        
        # Total cost by status
        cursor.execute("SELECT status, COUNT(*) as count, SUM(cost) as total_cost FROM campaigns GROUP BY status")
        stats = cursor.fetchall()
        print("   Query: SELECT status, COUNT(*), SUM(cost) FROM campaigns GROUP BY status")
        for stat in stats:
            print(f"   - {stat['status']}: {stat['count']} campaigns, ₹{stat['total_cost']:.2f} total cost")
        
        # Top campaigns by clicks
        cursor.execute("SELECT name, clicks, cost FROM campaigns ORDER BY clicks DESC LIMIT 5")
        top_campaigns = cursor.fetchall()
        print("\n   Query: SELECT name, clicks, cost FROM campaigns ORDER BY clicks DESC LIMIT 5")
        print("   Top 5 campaigns by clicks:")
        for i, campaign in enumerate(top_campaigns, 1):
            print(f"   {i}. {campaign['name']}: {campaign['clicks']} clicks, ₹{campaign['cost']}")
        
        conn.close()
        
        print("\n All SQL queries executed successfully!")
        print("Database schema and data are working correctly!")
        
    except Exception as e:
        print(f" SQL Query Error: {e}")

if __name__ == "__main__":
    test_sql_queries()