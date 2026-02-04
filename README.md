# Campaign Dashboard

A simple web app to track marketing campaigns. Built with Next.js for the frontend and FastAPI for the backend.

## What's Inside

- **Frontend**: Next.js app with a clean dashboard to view campaigns
- **Backend**: FastAPI server that serves campaign data
- **Database**: SQLite for development (can switch to PostgreSQL later)

## Features

- View all your marketing campaigns in a table
- Filter campaigns by status (Active/Paused)
- See total stats like clicks, cost, and impressions
- Responsive design that works on mobile too
- Indian Rupee currency formatting

## Getting Started

### Quick Setup

**For Windows:**
```bash
setup.bat
```

**For Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Setup

**Backend:**
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Then open:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## API Endpoints

- `GET /campaigns` - Get all campaigns
- `GET /campaigns?status=Active` - Get only active campaigns
- `GET /campaigns?status=Paused` - Get only paused campaigns

## Testing

Run the test script to make sure everything works:
```bash
python test_api.py
```

## Sample Data

The app comes with 10 sample campaigns with Indian festival themes like "Diwali Dhamaka Sale", "Cricket World Cup Promo", etc.

## Tech Stack

- Next.js 14 with TypeScript
- FastAPI with Python
- TailwindCSS for styling
- SQLite database

## Deployment

Ready to deploy on:
- Vercel (frontend)
- Railway (backend)

Check `DEPLOYMENT.md` for detailed instructions.