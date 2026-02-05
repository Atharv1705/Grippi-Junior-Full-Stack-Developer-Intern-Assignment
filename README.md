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

### Quick Deployment (Vercel)
1. Push this repository to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repository
3. Set **Root Directory** to `frontend`
4. Deploy!

Your app will be live with both frontend and API on the same domain.

### Local Development

**Option 1: Vercel Dev (Recommended)**
```bash
npm i -g vercel
vercel dev
```

**Option 2: Separate Frontend/Backend**
```bash
# Backend (Terminal 1)
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload

# Frontend (Terminal 2)
cd frontend
npm install
npm run dev
```

### Access the Application
- **Local**: http://localhost:3000
- **Deployed**: Your Vercel URL

## API Endpoints

- `GET /campaigns` - Get all campaigns
- `GET /campaigns?status=Active` - Get only active campaigns
- `GET /campaigns?status=Paused` - Get only paused campaigns

## Sample Data

The app comes with 10 sample campaigns including "Summer Sale", "Black Friday", "Holiday Special", etc. All costs are displayed in Indian Rupees (₹).

## Deployment

**Ready to deploy on Vercel!**

1. Push to GitHub
2. Import repository to Vercel
3. Set root directory to `frontend`
4. Deploy

Both frontend and API will be deployed together. See `DEPLOYMENT.md` for detailed instructions.