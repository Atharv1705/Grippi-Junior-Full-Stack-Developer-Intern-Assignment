# Campaign Dashboard

A simple web app to track marketing campaigns. Built with Next.js for the frontend and FastAPI for the backend.

## Project Structure

```
grippi-dashboard/
├── frontend/          # Next.js React application
├── backend/           # FastAPI Python application  
├── database/          # SQL scripts and database setup
├── DEPLOYMENT.md      # Deployment instructions
└── README.md
```

## Tech Stack

- **Frontend**: Next.js 14 with TypeScript
- **Backend**: FastAPI with Python
- **Database**: SQLite for development (PostgreSQL ready)
- **Styling**: TailwindCSS

## Features

- View all your marketing campaigns in a table
- Filter campaigns by status (Active/Paused)
- See total stats like clicks, cost, and impressions
- Responsive design that works on mobile too
- Indian Rupee currency formatting

## Getting Started

### Backend Setup
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## API Endpoints

- `GET /campaigns` - Get all campaigns
- `GET /campaigns?status=Active` - Get only active campaigns
- `GET /campaigns?status=Paused` - Get only paused campaigns

## Sample Data

The app comes with 10 sample campaigns including "Summer Sale", "Black Friday", "Holiday Special", etc. All costs are displayed in Indian Rupees (₹).

## Deployment

Ready to deploy on:
- **Frontend**: Vercel
- **Backend**: Railway

See `DEPLOYMENT.md` for detailed instructions.