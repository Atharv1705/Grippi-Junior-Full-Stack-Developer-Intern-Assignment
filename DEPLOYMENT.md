# Deployment Guide

## Backend Deployment (Railway)

1. **Prepare your backend**:
   ```bash
   cd backend
   # Ensure all files are ready
   ```

2. **Deploy to Railway**:
   - Go to [Railway.app](https://railway.app)
   - Connect your GitHub repository
   - Select the `backend` folder as the root
   - Railway will automatically detect Python and use the `requirements.txt`
   - Set environment variables if needed

3. **Configure Railway**:
   - The `railway.json` file is already configured
   - Railway will run: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Health check endpoint: `/health`

## Frontend Deployment (Vercel)

1. **Prepare your frontend**:
   ```bash
   cd frontend
   cp .env.example .env.local
   # Update NEXT_PUBLIC_API_URL with your Railway backend URL
   ```

2. **Deploy to Vercel**:
   - Go to [Vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Set the root directory to `frontend`
   - Add environment variable: `NEXT_PUBLIC_API_URL` with your Railway backend URL
   - Deploy

## Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

### Backend (Railway Dashboard)
No additional environment variables needed for basic setup.

## Database Setup

For production, you can:
1. Use Railway's PostgreSQL addon
2. Update the backend to use PostgreSQL instead of SQLite
3. Run the `database/setup.sql` script

## Testing Deployment

1. **Backend**: Visit `https://your-backend-url.railway.app/campaigns`
2. **Frontend**: Visit your Vercel URL and test the dashboard

## Troubleshooting

- **CORS Issues**: Ensure the frontend URL is added to CORS origins in `main.py`
- **API Connection**: Verify the `NEXT_PUBLIC_API_URL` environment variable
- **Database**: Check Railway logs for database connection issues