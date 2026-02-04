#!/usr/bin/env python3
"""
Quick test to check if our campaign API is working properly
"""

import requests
import json

def test_api():
    base_url = "http://localhost:8000"
    
    print("Testing Campaign API...")
    print("-" * 40)
    
    # Test 1: Check if API is up
    try:
        response = requests.get(f"{base_url}/")
        print(f"✓ API is running: {response.status_code}")
        print(f"  {response.json()['message']}")
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        return
    
    print()
    
    # Test 2: Get all campaigns
    try:
        response = requests.get(f"{base_url}/campaigns")
        data = response.json()
        print(f"✓ Got campaigns: {response.status_code}")
        print(f"  Found {data['total']} campaigns")
        if data['campaigns']:
            print(f"  First one: {data['campaigns'][0]['name']}")
    except Exception as e:
        print(f"✗ Failed to get campaigns: {e}")
    
    print()
    
    # Test 3: Filter active campaigns
    try:
        response = requests.get(f"{base_url}/campaigns?status=Active")
        data = response.json()
        print(f"✓ Active campaigns filter: {response.status_code}")
        print(f"  Active campaigns: {data['total']}")
    except Exception as e:
        print(f"✗ Active filter failed: {e}")
    
    print()
    
    # Test 4: Filter paused campaigns  
    try:
        response = requests.get(f"{base_url}/campaigns?status=Paused")
        data = response.json()
        print(f"✓ Paused campaigns filter: {response.status_code}")
        print(f"  Paused campaigns: {data['total']}")
    except Exception as e:
        print(f"✗ Paused filter failed: {e}")
    
    print()
    print("All tests completed!")

if __name__ == "__main__":
    test_api()