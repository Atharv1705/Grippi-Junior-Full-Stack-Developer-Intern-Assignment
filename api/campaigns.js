export default function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  // Handle OPTIONS request for CORS
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }
  
  // Only allow GET requests
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }
  
  // Get status filter from query parameters
  const { status } = req.query;
  
  // Sample campaign data
  const campaignsData = [
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
  ];
  
  // Filter by status if provided
  let filteredCampaigns = campaignsData;
  if (status) {
    filteredCampaigns = campaignsData.filter(campaign => campaign.status === status);
  }
  
  // Return response
  res.status(200).json({
    campaigns: filteredCampaigns,
    total: filteredCampaigns.length
  });
}