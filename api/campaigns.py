from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

def handler(request):
    # Parse URL and query parameters
    parsed_url = urlparse(request.url)
    query_params = parse_qs(parsed_url.query)
    status_filter = query_params.get('status', [None])[0]
    
    # Sample data for Vercel serverless function
    campaigns_data = [
        {"id": 1, "name": "Summer Sale", "status": "Active", "clicks": 150, "cost": 3799.25, "impressions": 1000},
        {"id": 2, "name": "Black Friday", "status": "Paused", "clicks": 320, "cost": 7399.50, "impressions": 2500},
        {"id": 3, "name": "Holiday Special", "status": "Active", "clicks": 275, "cost": 5559.75, "impressions": 1800},
        {"id": 4, "name": "Spring Launch", "status": "Paused", "clicks": 89, "cost": 1962.25, "impressions": 650},
        {"id": 5, "name": "Back to School", "status": "Active", "clicks": 445, "cost": 9279.80, "impressions": 3200},
        {"id": 6, "name": "Valentine's Day", "status": "Paused", "clicks": 198, "cost": 4614.40, "impressions": 1450},
        {"id": 7, "name": "Easter Promotion", "status": "Active", "clicks": 167, "cost": 3405.20, "impressions": 1100},
        {"id": 8, "name": "Mother's Day", "status": "Active", "clicks": 234, "cost": 6522.90, "impressions": 1750},
        {"id": 9, "name": "Father's Day", "status": "Paused", "clicks": 156, "cost": 3178.45, "impressions": 980},
        {"id": 10, "name": "End of Year", "status": "Active", "clicks": 389, "cost": 7902.60, "impressions": 2800}
    ]
    
    # Filter by status if provided
    if status_filter:
        filtered_campaigns = [c for c in campaigns_data if c['status'] == status_filter]
    else:
        filtered_campaigns = campaigns_data
    
    # Return response
    response = {
        "campaigns": filtered_campaigns,
        "total": len(filtered_campaigns)
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(response)
    }